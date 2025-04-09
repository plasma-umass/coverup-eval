# file: lib/ansible/utils/jsonrpc.py:112-113
# asked: {"lines": [112, 113], "branches": []}
# gained: {"lines": [112, 113], "branches": []}

import pytest
from ansible.utils.jsonrpc import JsonRpcServer

@pytest.fixture
def json_rpc_server():
    server = JsonRpcServer()
    server._identifier = 1  # Mocking the _identifier attribute
    return server

def test_internal_error_no_data(json_rpc_server):
    result = json_rpc_server.internal_error()
    assert result == json_rpc_server.error(-32603, 'Internal error', None)

def test_internal_error_with_data(json_rpc_server):
    data = {'key': 'value'}
    result = json_rpc_server.internal_error(data)
    assert result == json_rpc_server.error(-32603, 'Internal error', data)
