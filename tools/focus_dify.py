from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage


import re
import time
import json
import random
import requests
import hashlib
import hmac

absolute_http_url_regexp = re.compile(r"^https?://", re.I)
RANDOM_CHAR = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789"
class FocusDifyTool(Tool):
    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        self.headers = {
            "Authorization": None,
            "Content-Type":"application/json"
        }

    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        # tool_parameters["action"] == ""
        response = self._get("/df/rest/table/list")["data"]
        yield self.create_json_message(response)

    def _register_model(self):
        """注册模型"""
        {
            "language": "chinese",
            "model": {
                "type": "mysql",
                "version": "8.0",
                "tables": [
                {
                    "tableDisplayName": "test",
                    "tableName": "test",
                    "columns": [
                    {
                        "columnDisplayName": "name",
                        "columnName": "name",
                        "dataType": "string",
                        "aggregation": ""
                    },
                    {
                        "columnDisplayName": "address",
                        "columnName": "address",
                        "dataType": "string",
                        "aggregation": ""
                    },
                    {
                        "columnDisplayName": "age",
                        "columnName": "age",
                        "dataType": "int",
                        "aggregation": "SUM"
                    },
                    {
                        "columnDisplayName": "日期",
                        "columnName": "date",
                        "dataType": "timestamp",
                        "aggregation": ""
                    }
                    ]
                }
                ],
                "relations": []
            }
            }


    def _get(self, url, params:dict=None):
        self.headers["Authorization"] = "Bearer %s"%self.runtime.credentials["app_token"]
        url = self._build_url(self.runtime.credentials["datafocus_host"])
        response = requests.get(url, params=params, headers=self.headers, verify=False)
        response.raise_for_status()
        return response.json()

    def _post(self, url, body:dict=None, params:dict=None) -> dict:
        self.headers["Authorization"] = "Bearer %s"%self.runtime.credentials["app_token"]
        url = self._build_url(self.runtime.credentials["datafocus_host"])
        response = requests.post(url, params=params, json=body, headers=self.headers, verify=False)
        response.raise_for_status()
        return response.json()
        

    def _build_url(self, path):
        """ prepend url with hostname unless it's already an absolute URL """
        if absolute_http_url_regexp.match(path):
            return path
        else:
            if "/api/" in path:
                return "%s%s" % (self.base_url.split("?")[0], path)
            return "%s%s" % (self.base_url.split("?")[0], path)