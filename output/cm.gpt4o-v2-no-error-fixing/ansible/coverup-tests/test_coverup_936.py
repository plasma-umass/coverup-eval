# file: lib/ansible/utils/jsonrpc.py:91-97
# asked: {"lines": [], "branches": [[94, 96]]}
# gained: {"lines": [], "branches": [[94, 96]]}

import pytest
from ansible.utils.jsonrpc import JsonRpcServer

class TestJsonRpcServer:
    
    @pytest.fixture
    def json_rpc_server(self):
        return JsonRpcServer()

    def test_error_with_data(self, json_rpc_server, mocker):
        mocker.patch.object(json_rpc_server, 'header', return_value={'jsonrpc': '2.0', 'id': 1})
        response = json_rpc_server.error(123, 'An error occurred', data={'info': 'details'})
        assert response == {
            'jsonrpc': '2.0',
            'id': 1,
            'error': {
                'code': 123,
                'message': 'An error occurred',
                'data': {'info': 'details'}
            }
        }

    def test_error_without_data(self, json_rpc_server, mocker):
        mocker.patch.object(json_rpc_server, 'header', return_value={'jsonrpc': '2.0', 'id': 1})
        response = json_rpc_server.error(123, 'An error occurred')
        assert response == {
            'jsonrpc': '2.0',
            'id': 1,
            'error': {
                'code': 123,
                'message': 'An error occurred'
            }
        }
