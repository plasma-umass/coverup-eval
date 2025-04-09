# file: lib/ansible/utils/jsonrpc.py:100-101
# asked: {"lines": [100, 101], "branches": []}
# gained: {"lines": [100, 101], "branches": []}

import pytest
from ansible.utils.jsonrpc import JsonRpcServer

@pytest.fixture
def json_rpc_server():
    server = JsonRpcServer()
    server._identifier = 1  # Mocking the _identifier attribute
    return server

def test_parse_error_no_data(json_rpc_server):
    result = json_rpc_server.parse_error()
    assert result == json_rpc_server.error(-32700, 'Parse error', None)

def test_parse_error_with_data(json_rpc_server):
    data = {'key': 'value'}
    result = json_rpc_server.parse_error(data)
    assert result == json_rpc_server.error(-32700, 'Parse error', data)
