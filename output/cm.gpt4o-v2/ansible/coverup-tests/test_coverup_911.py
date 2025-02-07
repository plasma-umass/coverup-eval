# file: lib/ansible/utils/jsonrpc.py:106-107
# asked: {"lines": [106, 107], "branches": []}
# gained: {"lines": [106, 107], "branches": []}

import pytest
from ansible.utils.jsonrpc import JsonRpcServer

class MockJsonRpcServer(JsonRpcServer):
    def error(self, code, message, data=None):
        return {"code": code, "message": message, "data": data}

@pytest.fixture
def jsonrpc_server():
    return MockJsonRpcServer()

def test_invalid_request_no_data(jsonrpc_server):
    response = jsonrpc_server.invalid_request()
    assert response == {"code": -32600, "message": "Invalid request", "data": None}

def test_invalid_request_with_data(jsonrpc_server):
    data = {"key": "value"}
    response = jsonrpc_server.invalid_request(data)
    assert response == {"code": -32600, "message": "Invalid request", "data": data}
