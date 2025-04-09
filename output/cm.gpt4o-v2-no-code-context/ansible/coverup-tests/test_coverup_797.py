# file: lib/ansible/utils/jsonrpc.py:106-107
# asked: {"lines": [106, 107], "branches": []}
# gained: {"lines": [106, 107], "branches": []}

import pytest
from ansible.utils.jsonrpc import JsonRpcServer

@pytest.fixture
def json_rpc_server():
    server = JsonRpcServer()
    server._identifier = 1  # Mocking the _identifier attribute
    return server

def test_invalid_request_no_data(json_rpc_server):
    response = json_rpc_server.invalid_request()
    assert response == json_rpc_server.error(-32600, 'Invalid request', None)

def test_invalid_request_with_data(json_rpc_server):
    data = {'key': 'value'}
    response = json_rpc_server.invalid_request(data)
    assert response == json_rpc_server.error(-32600, 'Invalid request', data)
