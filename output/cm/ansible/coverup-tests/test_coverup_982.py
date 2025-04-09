# file lib/ansible/utils/jsonrpc.py:112-113
# lines [112, 113]
# branches []

import pytest
from ansible.utils.jsonrpc import JsonRpcServer

class MockJsonRpcServer(JsonRpcServer):
    def __init__(self):
        self._identifier = None

def test_internal_error():
    server = MockJsonRpcServer()
    error_response = server.internal_error(data="test_data")
    assert error_response == {
        'id': None,
        'jsonrpc': '2.0',
        'error': {
            'code': -32603,
            'message': 'Internal error',
            'data': 'test_data'
        }
    }
