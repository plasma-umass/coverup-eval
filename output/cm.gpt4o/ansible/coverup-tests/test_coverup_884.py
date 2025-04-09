# file lib/ansible/utils/jsonrpc.py:103-104
# lines [103, 104]
# branches []

import pytest
from ansible.utils.jsonrpc import JsonRpcServer

class TestJsonRpcServer:
    def test_method_not_found(self, mocker):
        server = JsonRpcServer()
        mock_error = mocker.patch.object(server, 'error', return_value='mocked_error_response')
        
        data = {'key': 'value'}
        response = server.method_not_found(data)
        
        mock_error.assert_called_once_with(-32601, 'Method not found', data)
        assert response == 'mocked_error_response'
