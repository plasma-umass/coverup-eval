# file: lib/ansible/utils/jsonrpc.py:112-113
# asked: {"lines": [113], "branches": []}
# gained: {"lines": [113], "branches": []}

import pytest
from ansible.utils.jsonrpc import JsonRpcServer

@pytest.fixture
def json_rpc_server():
    return JsonRpcServer()

def test_internal_error_no_data(json_rpc_server, mocker):
    mock_header = mocker.patch.object(JsonRpcServer, 'header', return_value={})
    response = json_rpc_server.internal_error()
    mock_header.assert_called_once()
    assert response == {
        'error': {
            'code': -32603,
            'message': 'Internal error'
        }
    }

def test_internal_error_with_data(json_rpc_server, mocker):
    mock_header = mocker.patch.object(JsonRpcServer, 'header', return_value={})
    data = {'info': 'some error info'}
    response = json_rpc_server.internal_error(data)
    mock_header.assert_called_once()
    assert response == {
        'error': {
            'code': -32603,
            'message': 'Internal error',
            'data': data
        }
    }
