# file: lib/ansible/utils/jsonrpc.py:106-107
# asked: {"lines": [107], "branches": []}
# gained: {"lines": [107], "branches": []}

import pytest
from ansible.utils.jsonrpc import JsonRpcServer

@pytest.fixture
def json_rpc_server():
    return JsonRpcServer()

def test_invalid_request_no_data(json_rpc_server, mocker):
    mocker.patch.object(json_rpc_server, 'header', return_value={})
    response = json_rpc_server.invalid_request()
    assert response['error']['code'] == -32600
    assert response['error']['message'] == 'Invalid request'
    assert 'data' not in response['error']

def test_invalid_request_with_data(json_rpc_server, mocker):
    mocker.patch.object(json_rpc_server, 'header', return_value={})
    data = {'key': 'value'}
    response = json_rpc_server.invalid_request(data)
    assert response['error']['code'] == -32600
    assert response['error']['message'] == 'Invalid request'
    assert response['error']['data'] == data
