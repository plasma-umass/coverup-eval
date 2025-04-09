# file: lib/ansible/module_utils/connection.py:184-202
# asked: {"lines": [184, 194, 196, 197, 198, 199, 200, 202], "branches": [[196, 197], [196, 202]]}
# gained: {"lines": [184, 194, 196, 197, 198, 199, 200, 202], "branches": [[196, 197], [196, 202]]}

import pytest
from ansible.module_utils.connection import Connection, ConnectionError
from ansible.module_utils._text import to_text

class MockConnection(Connection):
    def _exec_jsonrpc(self, name, *args, **kwargs):
        if name == "error_case":
            return {
                "error": {
                    "message": "An error occurred",
                    "code": 1234
                }
            }
        return {
            "result": "success"
        }

def test_rpc_success():
    conn = MockConnection(socket_path="/mock/path")
    result = conn.__rpc__("success_case")
    assert result == "success"

def test_rpc_error():
    conn = MockConnection(socket_path="/mock/path")
    with pytest.raises(ConnectionError) as excinfo:
        conn.__rpc__("error_case")
    assert str(excinfo.value) == to_text("An error occurred", errors='surrogate_then_replace')
    assert excinfo.value.code == 1234
