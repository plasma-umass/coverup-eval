# file: lib/ansible/module_utils/connection.py:184-202
# asked: {"lines": [194, 196, 197, 198, 199, 200, 202], "branches": [[196, 197], [196, 202]]}
# gained: {"lines": [194, 196, 197, 198, 199, 200, 202], "branches": [[196, 197], [196, 202]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.module_utils.connection import Connection, ConnectionError
from ansible.module_utils._text import to_text

@pytest.fixture
def connection(monkeypatch):
    # Mock the __init__ method to bypass the need for socket_path
    def mock_init(self, socket_path):
        self.socket_path = socket_path

    monkeypatch.setattr(Connection, '__init__', mock_init)
    return Connection('dummy_socket_path')

def test_rpc_success(connection, monkeypatch):
    # Mock the _exec_jsonrpc method to return a successful response
    def mock_exec_jsonrpc(name, *args, **kwargs):
        return {'result': 'success'}

    monkeypatch.setattr(connection, '_exec_jsonrpc', mock_exec_jsonrpc)

    result = connection.__rpc__('test_method')
    assert result == 'success'

def test_rpc_error_with_data(connection, monkeypatch):
    # Mock the _exec_jsonrpc method to return an error response with data
    def mock_exec_jsonrpc(name, *args, **kwargs):
        return {'error': {'code': 123, 'message': 'error occurred', 'data': 'detailed error data'}}

    monkeypatch.setattr(connection, '_exec_jsonrpc', mock_exec_jsonrpc)

    with pytest.raises(ConnectionError) as excinfo:
        connection.__rpc__('test_method')
    
    assert 'detailed error data' in str(excinfo.value)
    assert excinfo.value.code == 123

def test_rpc_error_without_data(connection, monkeypatch):
    # Mock the _exec_jsonrpc method to return an error response without data
    def mock_exec_jsonrpc(name, *args, **kwargs):
        return {'error': {'code': 456, 'message': 'another error occurred'}}

    monkeypatch.setattr(connection, '_exec_jsonrpc', mock_exec_jsonrpc)

    with pytest.raises(ConnectionError) as excinfo:
        connection.__rpc__('test_method')
    
    assert 'another error occurred' in str(excinfo.value)
    assert excinfo.value.code == 456
