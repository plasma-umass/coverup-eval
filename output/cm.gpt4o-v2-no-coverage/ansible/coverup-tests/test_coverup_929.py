# file: lib/ansible/utils/jsonrpc.py:100-101
# asked: {"lines": [100, 101], "branches": []}
# gained: {"lines": [100, 101], "branches": []}

import pytest
from ansible.utils.jsonrpc import JsonRpcServer

class MockJsonRpcServer(JsonRpcServer):
    def error(self, code, message, data=None):
        return {"code": code, "message": message, "data": data}

@pytest.fixture
def json_rpc_server():
    return MockJsonRpcServer()

def test_parse_error_no_data(json_rpc_server):
    result = json_rpc_server.parse_error()
    assert result == {"code": -32700, "message": "Parse error", "data": None}

def test_parse_error_with_data(json_rpc_server):
    data = {"info": "some error info"}
    result = json_rpc_server.parse_error(data)
    assert result == {"code": -32700, "message": "Parse error", "data": data}
