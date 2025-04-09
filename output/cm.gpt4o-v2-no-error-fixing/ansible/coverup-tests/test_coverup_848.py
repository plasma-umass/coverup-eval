# file: lib/ansible/utils/jsonrpc.py:106-107
# asked: {"lines": [107], "branches": []}
# gained: {"lines": [107], "branches": []}

import pytest
from ansible.utils.jsonrpc import JsonRpcServer

@pytest.fixture
def json_rpc_server():
    return JsonRpcServer()

def test_invalid_request(json_rpc_server, mocker):
    mock_error = mocker.patch.object(json_rpc_server, 'error', return_value="mocked_error_response")
    data = {"key": "value"}
    
    response = json_rpc_server.invalid_request(data)
    
    mock_error.assert_called_once_with(-32600, 'Invalid request', data)
    assert response == "mocked_error_response"
