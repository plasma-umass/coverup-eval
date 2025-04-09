# file lib/ansible/utils/jsonrpc.py:106-107
# lines [106, 107]
# branches []

import pytest
from ansible.utils.jsonrpc import JsonRpcServer

class TestJsonRpcServer:
    @pytest.fixture
    def json_rpc_server(self):
        return JsonRpcServer()

    def test_invalid_request(self, json_rpc_server, mocker):
        mock_error = mocker.patch.object(json_rpc_server, 'error', return_value='mocked_error_response')
        
        data = {'key': 'value'}
        response = json_rpc_server.invalid_request(data)
        
        mock_error.assert_called_once_with(-32600, 'Invalid request', data)
        assert response == 'mocked_error_response'
