# file: lib/ansible/utils/jsonrpc.py:109-110
# asked: {"lines": [109, 110], "branches": []}
# gained: {"lines": [109, 110], "branches": []}

import pytest
from ansible.utils.jsonrpc import JsonRpcServer

@pytest.fixture
def json_rpc_server():
    return JsonRpcServer()

def test_invalid_params(json_rpc_server, mocker):
    mock_header = mocker.patch.object(JsonRpcServer, 'header', return_value={})
    data = {'key': 'value'}
    
    response = json_rpc_server.invalid_params(data)
    
    mock_header.assert_called_once()
    assert response['error']['code'] == -32602
    assert response['error']['message'] == 'Invalid params'
    assert response['error']['data'] == data
