# file lib/ansible/utils/jsonrpc.py:109-110
# lines [109, 110]
# branches []

import pytest
from ansible.utils.jsonrpc import JsonRpcServer

@pytest.fixture
def json_rpc_server():
    return JsonRpcServer()

def test_invalid_params(json_rpc_server, mocker):
    mock_error = mocker.patch.object(JsonRpcServer, 'error', side_effect=lambda code, message, data: {'code': code, 'message': message, 'data': data})
    
    result = json_rpc_server.invalid_params()
    
    mock_error.assert_called_once_with(-32602, 'Invalid params', None)
    assert result == {'code': -32602, 'message': 'Invalid params', 'data': None}

    data = {'key': 'value'}
    result_with_data = json_rpc_server.invalid_params(data)
    
    mock_error.assert_called_with(-32602, 'Invalid params', data)
    assert result_with_data == {'code': -32602, 'message': 'Invalid params', 'data': data}
