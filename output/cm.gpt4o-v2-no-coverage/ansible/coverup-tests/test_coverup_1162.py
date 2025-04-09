# file: lib/ansible/module_utils/connection.py:93-101
# asked: {"lines": [94, 95, 96, 97, 98, 99, 100, 101], "branches": []}
# gained: {"lines": [94, 95, 96, 97, 98, 99, 100, 101], "branches": []}

import pytest
from ansible.module_utils.connection import exec_command, Connection, ConnectionError
from ansible.module_utils._text import to_text

class MockModule:
    def __init__(self, socket_path):
        self._socket_path = socket_path

class MockConnection(Connection):
    def _exec_jsonrpc(self, name, *args, **kwargs):
        if name == "exec_command" and args[0] == "raise_error":
            raise ConnectionError("Test error", code=2, err="Test error detail")
        return {"result": "command output"}

    def send(self, data):
        return data

@pytest.fixture
def mock_module():
    return MockModule("/fake/socket/path")

@pytest.fixture
def mock_connection(monkeypatch):
    def mock_init(self, socket_path):
        self.socket_path = socket_path
    monkeypatch.setattr(Connection, "__init__", mock_init)
    monkeypatch.setattr(Connection, "_exec_jsonrpc", MockConnection._exec_jsonrpc)
    monkeypatch.setattr(Connection, "send", MockConnection.send)

def test_exec_command_success(mock_module, mock_connection):
    code, out, err = exec_command(mock_module, "test command")
    assert code == 0
    assert out == "command output"
    assert err == ""

def test_exec_command_failure(mock_module, mock_connection):
    code, out, err = exec_command(mock_module, "raise_error")
    assert code == 2
    assert out == ""
    assert err == to_text("Test error detail", errors='surrogate_then_replace')
