# file: lib/ansible/utils/jsonrpc.py:109-110
# asked: {"lines": [110], "branches": []}
# gained: {"lines": [110], "branches": []}

import pytest
from ansible.utils.jsonrpc import JsonRpcServer

@pytest.fixture
def json_rpc_server():
    server = JsonRpcServer()
    server._identifier = 1  # Mocking the _identifier attribute
    return server

def test_invalid_params_no_data(json_rpc_server):
    result = json_rpc_server.invalid_params()
    assert result == json_rpc_server.error(-32602, 'Invalid params', None)

def test_invalid_params_with_data(json_rpc_server):
    data = {'key': 'value'}
    result = json_rpc_server.invalid_params(data)
    assert result == json_rpc_server.error(-32602, 'Invalid params', data)
