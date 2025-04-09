# file lib/ansible/utils/jsonrpc.py:112-113
# lines [112, 113]
# branches []

import pytest
from ansible.utils.jsonrpc import JsonRpcServer

@pytest.fixture
def json_rpc_server():
    return JsonRpcServer()

def test_internal_error(json_rpc_server, mocker):
    mock_error = mocker.patch.object(json_rpc_server, 'error', return_value='mocked_error')
    data = {'key': 'value'}
    
    result = json_rpc_server.internal_error(data)
    
    mock_error.assert_called_once_with(-32603, 'Internal error', data)
    assert result == 'mocked_error'
