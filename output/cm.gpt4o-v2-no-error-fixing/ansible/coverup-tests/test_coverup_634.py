# file: lib/ansible/utils/jsonrpc.py:103-104
# asked: {"lines": [103, 104], "branches": []}
# gained: {"lines": [103, 104], "branches": []}

import pytest
from ansible.utils.jsonrpc import JsonRpcServer

class TestJsonRpcServer:
    
    def test_method_not_found(self, mocker):
        server = JsonRpcServer()
        mock_error = mocker.patch.object(server, 'error', return_value='error_response')
        
        result = server.method_not_found(data={'key': 'value'})
        
        mock_error.assert_called_once_with(-32601, 'Method not found', {'key': 'value'})
        assert result == 'error_response'
