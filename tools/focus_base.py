# -*- coding: utf-8 -*-
# @Time    : 2025/1/21 13:57
# @Author  : ShaoJK
# @File    : focus_base.py
# @Remark  :
import json
import uuid
from collections.abc import Generator
from typing import Any

import requests
from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from tools.constants import Aggregation, DataType


class FocusAPIError(Exception):
    def __init__(self, response):
        self.message = response.get("exception")
        self.err_code = response.get("errCode")

    def __str__(self):
        return "Focus API Error：%s %s" % (self.err_code, self.message)


class FocusBaseTool(Tool):
    STORAGE_SIZE = 50
    STORAGE_KEY = "StorageKey"
    STORAGE_VALUE = "StorageValue"
    STORAGE_INDEX = 'StorageIndex'

    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        self.headers = {
            "Authorization": None,
            "Content-Type": "application/json"
        }
        self.tool_parameters = None
        self.conversation_id = None
        self.chat_id = None
        self.conversation_ids = []
        self.storage_index = int(self.__get_storage(self.STORAGE_INDEX, 0))
        if not self.storage_index:
            self.storage_index = 0
        for i in range(self.STORAGE_SIZE):
            self.conversation_ids.append(self.__get_storage_key(i))

    def _invoke(self, tool_parameters: dict) -> Generator[ToolInvokeMessage]:
        self.tool_parameters = tool_parameters
        self.conversation_id = self.get_param("conversation_id", "")
        if self.__class__.__name__ == FocusBaseTool.__name__:
            return self.list_table(tool_parameters)

    def need_reinit(self, tbl_name=None, language=None):
        """判断是否需要重新初始化"""
        if not tbl_name or tbl_name != self.get_param("tableName"):
            return True
        if not language or language.lower() != self.get_param("language").lower():
            return True
        return False

    def __get_storage(self, key, default=None):
        try:
            return self.session.storage.get(key).decode()
        except Exception:
            return default

    def __set_storage(self, key, value):
        self.session.storage.set(key, value.encode())

    def __get_storage_key(self, idx):
        return self.__get_storage(self.STORAGE_KEY + str(idx))

    def __set_storage_key(self, idx, value: str):
        self.__set_storage(self.STORAGE_KEY + str(idx), value)

    def __get_storage_value(self, idx):
        return self.__get_storage(self.STORAGE_VALUE + str(idx))

    def __set_storage_value(self, idx, value: str):
        self.__set_storage(self.STORAGE_VALUE + str(idx), value)

    def next_index(self) -> int:
        return self.storage_index + 1 if self.storage_index + 1 < self.STORAGE_SIZE else 0

    def get_storage_info(self) -> dict:
        """从storage中恢复指定conversation_id保存的信息"""
        if self.conversation_id and self.conversation_id in self.conversation_ids:
            self.storage_index = self.conversation_ids.index(self.conversation_id)
            try:
                return json.loads(self.__get_storage_value(self.storage_index))
            except Exception as e:
                print(e)
                pass
        else:
            self.storage_index = self.next_index()
            self.__set_storage(self.STORAGE_INDEX, str(self.storage_index))  # 及时更新storage_index
            self.conversation_ids[self.storage_index] = self.conversation_id
            self.__set_storage_key(self.storage_index, self.conversation_id)
        return {}

    def set_storage_info(self, data):
        """向storage中保存conversation_id的数据"""
        self.__set_storage_key(self.storage_index, self.conversation_id)
        self.__set_storage_value(self.storage_index, json.dumps(data, ensure_ascii=False))

    def list_table(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        """获取表列表"""
        datasource = self.parse_datasource_config(tool_parameters)
        tbl_name = self.get_param("tableName", "")
        if datasource:
            response = self.post("/df/rest/datasource/tables", params={"name": tbl_name}, body=datasource)["data"]
        else:
            response = self.get("/df/rest/table/list", params={"name": tbl_name})["data"]
        for tbl in response:
            yield self.create_json_message({"name": tbl["tblDisplayName"], "numColumns": len(tbl['columns'])})

    def get_param(self, key, default=None):
        param = self.tool_parameters.get(key)
        if param:
            return param
        else:
            return default

    @staticmethod
    def __check_datasource_param(tool_parameters, key):
        param = tool_parameters.get(key)
        if param:
            return param
        else:
            raise ValueError("%s is necessary, if you assigned datasource type." % key.capitalize())

    def parse_datasource_config(self, tool_parameters: dict[str, Any]) -> dict:
        db_type = self.get_param("type")
        if not db_type:
            return None
        name = self.get_param("name")
        if not name:
            name = "Dify-%s-%s" % (db_type, str(uuid.uuid4())[:8])
        host = self.__check_datasource_param(tool_parameters, "host")
        port = self.__check_datasource_param(tool_parameters, "port")
        user = self.__check_datasource_param(tool_parameters, "user")
        password = self.__check_datasource_param(tool_parameters, "password")
        db = self.__check_datasource_param(tool_parameters, "db")
        return {
            "type": db_type,
            "name": name,
            "description": self.get_param("description"),
            "schemaName": self.get_param("schema"),
            "host": host,
            "port": port,
            "user": user,
            "password": password,
            "db": db,
            "jdbcSuffix": self.get_param("jdbc")
        }

    def get(self, url, params: dict = None, verify=True):
        print("Get: %s" % url)
        self.headers["Authorization"] = "Bearer %s" % self.runtime.credentials["app_token"]
        response = requests.get(self.__build_url(url), params=params, headers=self.headers, verify=False)
        response.raise_for_status()
        response = response.json()
        if verify and response["errCode"] != 0:
            raise FocusAPIError(response)
        return response

    def post(self, url, body: dict = None, params: dict = None, verify=True) -> dict:
        print("Post: %s" % url)
        self.headers["Authorization"] = "Bearer %s" % self.runtime.credentials["app_token"]
        response = requests.post(self.__build_url(url), params=params, json=body, headers=self.headers, verify=False)
        response.raise_for_status()
        response = response.json()
        if verify and response["errCode"] != 0:
            raise FocusAPIError(response)
        return response

    def __build_url(self, path):
        return self.runtime.credentials["datafocus_host"] + path


class FocusGPTTool(FocusBaseTool):
    STORAGE_KEY = "StorageGPTKey"
    STORAGE_VALUE = "StorageGPTValue"
    STORAGE_INDEX = 'StorageGPTIndex'

    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        super()._invoke(tool_parameters)
        action = self.get_param("action")
        if action == "listTables":
            return self.list_table(tool_parameters)
        elif action == "chat":
            return self.chat(tool_parameters)
        else:
            raise ValueError("Unexpected action type: %s" % action)

    def init(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        """初始化FocusGPT上下文"""
        language = self.get_param("language", "chinese")
        tbl_name = self.get_param("tableName", "")
        datasource = self.parse_datasource_config(tool_parameters)
        body = {"language": language.lower()}
        if datasource:
            body["dataSource"] = datasource
        if tbl_name:
            body["names"] = [tbl_name]
        else:
            raise KeyError("TableName cannot be empty.")
        response = self.post("/df/rest/gpt/init", body=body)

        data = {"tblName": tbl_name, "language": language}
        if response["errCode"] == 0:
            self.chat_id = response["data"]
            data["chatId"] = self.chat_id
            self.set_storage_info(data)
            yield self.create_text_message("已选择数据表[%s]" % tbl_name)
        elif response["errCode"] == 1008:
            self.set_storage_info(data)
            yield self.create_text_message("选择的表不存在")
        else:
            raise ValueError("Unexpected errCode: %s" % response["errCode"])

    def chat(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        data = self.get_storage_info()
        self.chat_id = data.get("chatId")
        tbl_name = data.get("tblName")
        language = data.get("language")
        query = self.get_param("query")
        if self.need_reinit(tbl_name, language):
            for output in self.init(tool_parameters):
                yield output
        if self.chat_id and query:
            response = self.post("/df/rest/gpt/data", body={"input": query, "chatId": self.chat_id})
            if response["errCode"] == 1001:
                for output in self.init(tool_parameters):
                    yield output
                response = self.post("/df/rest/gpt/data", body={"input": query, "chatId": self.chat_id})
            yield self.create_json_message(response["data"]["content"])


class FocusSQLTool(FocusBaseTool):
    STORAGE_KEY = "StorageSQLKey"
    STORAGE_VALUE = "StorageSQLValue"
    STORAGE_INDEX = 'StorageSQLIndex'

    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        super()._invoke(tool_parameters)
        action = self.get_param("action")
        if action == "listTables":
            return self.list_table(tool_parameters)
        elif action == "chat":
            return self.chat(tool_parameters)
        else:
            raise ValueError("Unexpected action type: %s" % action)

    def init(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        """初始化FocusGPT上下文"""
        language = self.get_param("language", "chinese")
        tbl_name = self.get_param("tableName")
        output_sql_type = self.get_param("outputSqlType", "mysql")
        model = self.get_param("model")
        datasource = self.parse_datasource_config(tool_parameters)
        body = {"language": language.lower()}
        if model:
            body["model"] = model
        else:
            body["model"] = {
                "type": output_sql_type.lower(),
                "version": "8.0",
                "tables": [self.get_table_model(tbl_name, datasource)],
                "relations": []
            }
        response = self.post("/df/rest/gpt/start", body=body)

        data = {"tblName": tbl_name, "language": language}
        if response["errCode"] == 0:
            self.chat_id = response["data"]
            data["chatId"] = self.chat_id
            self.set_storage_info(data)
            yield self.create_text_message("已初始化表[%s]" % tbl_name)
        else:
            raise ValueError(
                "Unexpected errCode: %s, with %s" % (response["errCode"], json.dumps(response, ensure_ascii=False)))

    def chat(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        data = self.get_storage_info()
        self.chat_id = data.get("chatId")
        tbl_name = data.get("tblName")
        language = data.get("language")
        query = self.get_param("query")
        if self.need_reinit(tbl_name, language):
            for output in self.init(tool_parameters):
                yield output
        if self.chat_id and query:
            response = self.post("/df/rest/gpt/chat", body={"input": query, "chatId": self.chat_id})
            if response["errCode"] == 1001:
                for output in self.init(tool_parameters):
                    yield output
                response = self.post("/df/rest/gpt/chat", body={"input": query, "chatId": self.chat_id})
            yield self.create_json_message(response["data"])

    def get_table_model(self, tbl_name, datasource=None):
        """获取并构建表的数据模型"""
        if datasource:
            # 从外部数据源中获取表模型
            for table in self.post("/df/rest/datasource/tables", params={"name": tbl_name}, body=datasource)["data"]:
                if table["tblDisplayName"] == tbl_name:
                    return self.build_table_model(table, is_external=True)
        else:
            # 从datafocus中获取表结构
            for table in self.get("/df/rest/table/list", params={"name": tbl_name})["data"]:
                if table["tblDisplayName"] == tbl_name:
                    return self.build_table_model(table)

    @staticmethod
    def build_table_model(table_info: dict, is_external=False) -> dict:
        columns = []
        table_model = {
            "tableDisplayName": table_info["tblDisplayName"],
            "tableName": table_info["tblName"],
            "columns": columns
        }
        for col_info in table_info["columns"]:
            columns.append({
                "columnDisplayName": col_info["colDisplayName"],
                "columnName": col_info["colName"],
                "dataType": DataType.map_data_type(col_info["dataType"]) if is_external else col_info["dataType"],
                "aggregation": Aggregation.get_default_aggregation(col_info["dataType"])
            })
        return table_model
