# file lib/ansible/utils/jsonrpc.py:106-107
# lines [107]
# branches []

import pytest
from ansible.utils.jsonrpc import JsonRpcServer

class MockJsonRpcServer(JsonRpcServer):
    def __init__(self):
        self._identifier = None

def test_invalid_request():
    server = MockJsonRpcServer()
    data = {'some': 'data'}
    expected_response = {
        'jsonrpc': '2.0',
        'error': {
            'code': -32600,
            'message': 'Invalid request',
            'data': data
        },
        'id': None
    }
    response = server.invalid_request(data)
    assert response == expected_response
