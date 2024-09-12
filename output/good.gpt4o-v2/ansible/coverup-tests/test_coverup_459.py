# file: lib/ansible/utils/jsonrpc.py:91-97
# asked: {"lines": [91, 92, 93, 94, 95, 96, 97], "branches": [[94, 95], [94, 96]]}
# gained: {"lines": [91, 92, 93, 94, 95, 96, 97], "branches": [[94, 95], [94, 96]]}

import pytest
from ansible.utils.jsonrpc import JsonRpcServer

@pytest.fixture
def json_rpc_server():
    return JsonRpcServer()

def test_error_with_data(json_rpc_server, mocker):
    mocker.patch.object(json_rpc_server, 'header', return_value={})
    response = json_rpc_server.error(123, "Test message", data="Test data")
    assert response == {
        'error': {
            'code': 123,
            'message': "Test message",
            'data': "Test data"
        }
    }

def test_error_without_data(json_rpc_server, mocker):
    mocker.patch.object(json_rpc_server, 'header', return_value={})
    response = json_rpc_server.error(123, "Test message")
    assert response == {
        'error': {
            'code': 123,
            'message': "Test message"
        }
    }
