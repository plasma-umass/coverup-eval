# file: lib/ansible/utils/jsonrpc.py:103-104
# asked: {"lines": [103, 104], "branches": []}
# gained: {"lines": [103, 104], "branches": []}

import pytest
from ansible.utils.jsonrpc import JsonRpcServer

class TestJsonRpcServer:
    
    @pytest.fixture
    def json_rpc_server(self):
        return JsonRpcServer()

    def test_method_not_found(self, json_rpc_server, mocker):
        mock_error = mocker.patch.object(json_rpc_server, 'error', return_value='error_response')
        
        data = {'key': 'value'}
        response = json_rpc_server.method_not_found(data)
        
        mock_error.assert_called_once_with(-32601, 'Method not found', data)
        assert response == 'error_response'
