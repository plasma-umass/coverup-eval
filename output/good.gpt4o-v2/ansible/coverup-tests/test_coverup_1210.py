# file: lib/ansible/module_utils/connection.py:93-101
# asked: {"lines": [94, 95, 96, 97, 98, 99, 100, 101], "branches": []}
# gained: {"lines": [94, 95, 96, 97, 98, 99, 100, 101], "branches": []}

import pytest
from ansible.module_utils.connection import exec_command, Connection, ConnectionError
from ansible.module_utils._text import to_text

class MockModule:
    def __init__(self, socket_path):
        self._socket_path = socket_path

def test_exec_command_success(monkeypatch):
    def mock__rpc__(self, name, *args, **kwargs):
        return "command output"

    monkeypatch.setattr(Connection, "__rpc__", mock__rpc__)
    module = MockModule("/fake/socket/path")
    code, out, err = exec_command(module, "fake command")
    
    assert code == 0
    assert out == "command output"
    assert err == ""

def test_exec_command_connection_error(monkeypatch):
    def mock__rpc__(self, name, *args, **kwargs):
        raise ConnectionError("connection failed", code=2, err="error details")

    monkeypatch.setattr(Connection, "__rpc__", mock__rpc__)
    module = MockModule("/fake/socket/path")
    code, out, err = exec_command(module, "fake command")
    
    assert code == 2
    assert out == ""
    assert err == to_text("error details", errors='surrogate_then_replace')

def test_exec_command_connection_error_no_code(monkeypatch):
    def mock__rpc__(self, name, *args, **kwargs):
        raise ConnectionError("connection failed")

    monkeypatch.setattr(Connection, "__rpc__", mock__rpc__)
    module = MockModule("/fake/socket/path")
    code, out, err = exec_command(module, "fake command")
    
    assert code == 1
    assert out == ""
    assert err == to_text("connection failed", errors='surrogate_then_replace')
