# file: lib/ansible/utils/jsonrpc.py:112-113
# asked: {"lines": [112, 113], "branches": []}
# gained: {"lines": [112, 113], "branches": []}

import pytest
from ansible.utils.jsonrpc import JsonRpcServer

@pytest.fixture
def json_rpc_server():
    return JsonRpcServer()

def test_internal_error_no_data(json_rpc_server, mocker):
    mocker.patch.object(json_rpc_server, 'header', return_value={})
    response = json_rpc_server.internal_error()
    assert response['error']['code'] == -32603
    assert response['error']['message'] == 'Internal error'
    assert 'data' not in response['error']

def test_internal_error_with_data(json_rpc_server, mocker):
    mocker.patch.object(json_rpc_server, 'header', return_value={})
    data = {'info': 'some error details'}
    response = json_rpc_server.internal_error(data)
    assert response['error']['code'] == -32603
    assert response['error']['message'] == 'Internal error'
    assert response['error']['data'] == data
