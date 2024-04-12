# file lib/ansible/utils/jsonrpc.py:103-104
# lines [103, 104]
# branches []

import pytest
from ansible.utils.jsonrpc import JsonRpcServer

class MockJsonRpcServer(JsonRpcServer):
    def __init__(self):
        self._identifier = None

def test_method_not_found():
    server = MockJsonRpcServer()
    data = {'some': 'data'}
    expected_error = {
        'jsonrpc': '2.0',
        'error': {
            'code': -32601,
            'message': 'Method not found',
            'data': data
        },
        'id': None
    }
    assert server.method_not_found(data) == expected_error
