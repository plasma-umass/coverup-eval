# file lib/ansible/utils/jsonrpc.py:91-97
# lines [91, 92, 93, 94, 95, 96, 97]
# branches ['94->95', '94->96']

import pytest
from ansible.utils.jsonrpc import JsonRpcServer

class MockJsonRpcServer(JsonRpcServer):
    def __init__(self):
        self._identifier = 1

@pytest.fixture
def json_rpc_server():
    return MockJsonRpcServer()

def test_error_with_data(json_rpc_server):
    code = 123
    message = "Test error"
    data = {"info": "Additional data"}
    
    response = json_rpc_server.error(code, message, data)
    
    assert 'error' in response
    assert response['error']['code'] == code
    assert response['error']['message'] == message
    assert response['error']['data'] == data

def test_error_without_data(json_rpc_server):
    code = 456
    message = "Another test error"
    
    response = json_rpc_server.error(code, message)
    
    assert 'error' in response
    assert response['error']['code'] == code
    assert response['error']['message'] == message
    assert 'data' not in response['error']
