# file: lib/ansible/utils/jsonrpc.py:103-104
# asked: {"lines": [103, 104], "branches": []}
# gained: {"lines": [103, 104], "branches": []}

import pytest
from ansible.utils.jsonrpc import JsonRpcServer

class TestJsonRpcServer:
    @pytest.fixture
    def json_rpc_server(self):
        server = JsonRpcServer()
        server._identifier = 1  # Mocking the _identifier attribute
        return server

    def test_method_not_found(self, json_rpc_server, mocker):
        data = {"key": "value"}
        mocker.patch.object(json_rpc_server, 'error', return_value={
            'jsonrpc': '2.0',
            'id': json_rpc_server._identifier,
            'error': {
                'code': -32601,
                'message': 'Method not found',
                'data': data
            }
        })
        result = json_rpc_server.method_not_found(data)
        assert result['error']['code'] == -32601
        assert result['error']['message'] == 'Method not found'
        assert result['error']['data'] == data
