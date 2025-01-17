import uuid
from collections.abc import Generator
from typing import Any

import requests
from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage


class FocusDifyTool(Tool):
    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        self.headers = {
            "Authorization": None,
            "Content-Type": "application/json"
        }
        self.chatId = None
        self.tbl_name = None

    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        action = tool_parameters.get("action")
        print(self.session.conversation_id)
        if action == "listTables":
            return self.list_table(tool_parameters)
        elif action == "init":
            return self.init(tool_parameters)
        elif action == "chat":
            return self.chat(tool_parameters)
        else:
            raise ValueError("Unexpected action type: %s" % action)

    def list_table(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        """获取表列表"""
        datasource = self.parse_datasource_config(tool_parameters)
        if datasource:
            response = self._post("/df/rest/datasource/tables", body=datasource)["data"]
        else:
            response = self._get("/df/rest/table/list", params={"name": tool_parameters.get("tableName", "")})["data"]
        for tbl in response:
            yield self.create_json_message({"name": tbl["tblDisplayName"], "numColumns": len(tbl['columns'])})

    @staticmethod
    def get_checked_param(tool_parameters, key):
        param = tool_parameters.get(key)
        if param:
            return param
        else:
            raise ValueError("%s is necessary, if you assigned datasource type." % key.capitalize())

    def parse_datasource_config(self, tool_parameters: dict[str, Any]) -> dict:
        db_type = tool_parameters.get("type")
        if not db_type:
            return None
        name = tool_parameters.get("name")
        if not name:
            name = "Dify-%s-%s" % (db_type, str(uuid.uuid4())[:8])
        host = self.get_checked_param(tool_parameters, "host")
        port = self.get_checked_param(tool_parameters, "port")
        user = self.get_checked_param(tool_parameters, "user")
        password = self.get_checked_param(tool_parameters, "password")
        db = self.get_checked_param(tool_parameters, "db")
        return {
            "type": db_type,
            "name": name,
            "description": tool_parameters.get("description"),
            "schemaName": tool_parameters.get("schema"),
            "host": host,
            "port": port,
            "user": user,
            "password": password,
            "db": db,
            "jdbcSuffix": tool_parameters.get("jdbc")
        }

    def init(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        """初始化FocusGPT上下文"""
        self.tbl_name = tool_parameters.get("tableName")
        datasource = self.parse_datasource_config(tool_parameters)
        self.set_variables(tbl_name=self.tbl_name)
        response = self._post("/df/rest/gpt/init", body={
            "names": [self.tbl_name],
            "dataSource": datasource
        })
        if response["errCode"] == 0:
            self.chatId = response["data"]
            self.set_variables(chatId=self.chatId)
            print(self.chatId, self.tbl_name)
            yield self.create_text_message("已选择数据表[%s]" % self.tbl_name)
        elif response["errCode"] == 1008:
            yield self.create_text_message("选择的表不存在")
        else:
            raise ValueError("Unexpected errCode: %s" % response["errCode"])

    def chat(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        self.chatId, self.tbl_name = self.get_variables("chatId", "tbl_name")
        print(self.chatId, self.tbl_name)
        query = tool_parameters["query"]
        if self.tbl_name != tool_parameters["tableName"]:
            for output in self.init(tool_parameters):
                yield output
        if self.chatId and query:
            response = self._post("/df/rest/gpt/data", body={"input": query, "chatId": self.chatId})
            if response["errCode"] == 1001:
                for output in self.init(tool_parameters):
                    yield output
                response = self._post("/df/rest/gpt/data", body={"input": query, "chatId": self.chatId})
            yield self.create_json_message(response["data"]["content"])

    def get_variables(self, *args):
        """获取持久化存储变量"""
        values = []
        for arg in args:
            try:
                values.append(self.session.storage.get(arg).decode('utf-8'))
            except Exception:
                values.append(None)
        return tuple(values)

    def set_variables(self, **kwargs):
        """设置持久化存储变量"""
        for key, value in kwargs.items():
            self.session.storage.set(key, value.encode('utf-8'))

    def _get(self, url, params: dict = None):
        print("Get: %s" % url)
        self.headers["Authorization"] = "Bearer %s" % self.runtime.credentials["app_token"]
        response = requests.get(self._build_url(url), params=params, headers=self.headers, verify=False)
        response.raise_for_status()
        return response.json()

    def _post(self, url, body: dict = None, params: dict = None) -> dict:
        print("Post: %s" % url)
        self.headers["Authorization"] = "Bearer %s" % self.runtime.credentials["app_token"]
        response = requests.post(self._build_url(url), params=params, json=body, headers=self.headers, verify=False)
        response.raise_for_status()
        return response.json()

    def _build_url(self, path):
        return self.runtime.credentials["datafocus_host"] + path
