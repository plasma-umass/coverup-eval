# file lib/ansible/utils/jsonrpc.py:109-110
# lines [110]
# branches []

import pytest
from ansible.utils.jsonrpc import JsonRpcServer

@pytest.fixture
def json_rpc_server(mocker):
    mocker.patch.object(JsonRpcServer, '__init__', return_value=None)
    server = JsonRpcServer()
    server._identifier = None  # Mock the _identifier attribute
    return server

def test_invalid_params(json_rpc_server):
    data = {'param': 'value'}
    expected_response = {
        'jsonrpc': '2.0',
        'error': {
            'code': -32602,
            'message': 'Invalid params',
            'data': data
        },
        'id': None
    }
    response = json_rpc_server.invalid_params(data)
    assert response == expected_response, "The response should match the expected error structure."
