# file: lib/ansible/utils/jsonrpc.py:112-113
# asked: {"lines": [112, 113], "branches": []}
# gained: {"lines": [112, 113], "branches": []}

import pytest
from ansible.utils.jsonrpc import JsonRpcServer

class MockJsonRpcServer(JsonRpcServer):
    def error(self, code, message, data=None):
        return {"code": code, "message": message, "data": data}

@pytest.fixture
def jsonrpc_server():
    return MockJsonRpcServer()

def test_internal_error_no_data(jsonrpc_server):
    response = jsonrpc_server.internal_error()
    assert response == {"code": -32603, "message": "Internal error", "data": None}

def test_internal_error_with_data(jsonrpc_server):
    data = {"info": "some error details"}
    response = jsonrpc_server.internal_error(data)
    assert response == {"code": -32603, "message": "Internal error", "data": data}
