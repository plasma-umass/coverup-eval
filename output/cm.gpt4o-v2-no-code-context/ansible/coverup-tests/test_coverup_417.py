# file: lib/ansible/utils/jsonrpc.py:91-97
# asked: {"lines": [91, 92, 93, 94, 95, 96, 97], "branches": [[94, 95], [94, 96]]}
# gained: {"lines": [91, 92, 93, 94, 95, 96, 97], "branches": [[94, 95], [94, 96]]}

import pytest
from ansible.utils.jsonrpc import JsonRpcServer

@pytest.fixture
def json_rpc_server():
    server = JsonRpcServer()
    server._identifier = 1  # Mocking the _identifier attribute
    return server

def test_error_with_data(json_rpc_server):
    response = json_rpc_server.error(123, "Test error", data="Additional data")
    assert response['error']['code'] == 123
    assert response['error']['message'] == "Test error"
    assert response['error']['data'] == "Additional data"

def test_error_without_data(json_rpc_server):
    response = json_rpc_server.error(123, "Test error")
    assert response['error']['code'] == 123
    assert response['error']['message'] == "Test error"
    assert 'data' not in response['error']
