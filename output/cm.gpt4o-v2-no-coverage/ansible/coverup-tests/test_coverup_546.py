# file: lib/ansible/module_utils/connection.py:127-133
# asked: {"lines": [127, 128, 129, 130, 131, 132, 133], "branches": [[131, 132], [131, 133]]}
# gained: {"lines": [127, 128, 129, 130, 131, 132, 133], "branches": [[131, 132], [131, 133]]}

import pytest
from functools import partial
from ansible.module_utils.connection import Connection, ConnectionError

class MockConnection(Connection):
    def __init__(self):
        self._exec_jsonrpc_called = False

    def _exec_jsonrpc(self, name, *args, **kwargs):
        self._exec_jsonrpc_called = True
        if name == "error_method":
            return {'error': {'message': 'error occurred', 'code': 123}}
        return {'result': 'success'}

def test_get_existing_attr():
    conn = MockConnection()
    conn.existing_attr = "value"
    assert conn.existing_attr == "value"

def test_get_non_existing_attr():
    conn = MockConnection()
    rpc_method = conn.some_method
    assert isinstance(rpc_method, partial)
    rpc_method()
    assert conn._exec_jsonrpc_called

def test_get_non_existing_private_attr():
    conn = MockConnection()
    with pytest.raises(AttributeError) as excinfo:
        _ = conn._private_method
    assert str(excinfo.value) == "'MockConnection' object has no attribute '_private_method'"

def test_rpc_method_success():
    conn = MockConnection()
    result = conn.some_method()
    assert result == 'success'

def test_rpc_method_error():
    conn = MockConnection()
    with pytest.raises(ConnectionError) as excinfo:
        conn.error_method()
    assert str(excinfo.value) == 'error occurred'
    assert excinfo.value.code == 123
