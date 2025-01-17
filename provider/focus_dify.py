from typing import Any

from dify_plugin import ToolProvider
from dify_plugin.errors.tool import ToolProviderCredentialValidationError
from tools.focus_dify import FocusDifyTool


class FocusDifyProvider(ToolProvider):
    def _validate_credentials(self, credentials: dict[str, Any]) -> None:
        try:
            """
            IMPLEMENT YOUR VALIDATION HERE
            """
            for _ in FocusDifyTool.from_credentials(credentials).invoke(
                tool_parameters={"query": "test"},
            ):
                pass

        except Exception as e:
            raise ToolProviderCredentialValidationError(str(e))
