# file lib/ansible/utils/jsonrpc.py:100-101
# lines [100, 101]
# branches []

import pytest
from ansible.utils.jsonrpc import JsonRpcServer

class MockJsonRpcServer(JsonRpcServer):
    def __init__(self):
        self._identifier = None

@pytest.fixture
def json_rpc_server():
    return MockJsonRpcServer()

def test_parse_error(json_rpc_server):
    data = {'detail': 'Invalid JSON'}
    json_rpc_server._identifier = 1  # Set an identifier for the test
    expected_error = {
        'jsonrpc': '2.0',
        'id': 1,
        'error': {
            'code': -32700,
            'message': 'Parse error',
            'data': data
        }
    }
    assert json_rpc_server.parse_error(data) == expected_error
