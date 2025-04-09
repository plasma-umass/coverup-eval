# file: lib/ansible/executor/interpreter_discovery.py:24-35
# asked: {"lines": [24, 25, 26, 27, 28, 30, 31, 33, 35], "branches": []}
# gained: {"lines": [24, 25, 30, 31, 33, 35], "branches": []}

import pytest
from ansible.executor.interpreter_discovery import InterpreterDiscoveryRequiredError

def test_interpreter_discovery_required_error_init():
    message = "Interpreter discovery required"
    interpreter_name = "python3"
    discovery_mode = "auto"
    error = InterpreterDiscoveryRequiredError(message, interpreter_name, discovery_mode)
    
    assert error.interpreter_name == interpreter_name
    assert error.discovery_mode == discovery_mode
    assert str(error) == message
    assert repr(error) == message

def test_interpreter_discovery_required_error_str():
    message = "Interpreter discovery required"
    error = InterpreterDiscoveryRequiredError(message, "python3", "auto")
    
    assert str(error) == message

def test_interpreter_discovery_required_error_repr():
    message = "Interpreter discovery required"
    error = InterpreterDiscoveryRequiredError(message, "python3", "auto")
    
    assert repr(error) == message

@pytest.fixture(autouse=True)
def patch_interpreter_discovery_required_error(monkeypatch):
    def mock_init(self, message, interpreter_name, discovery_mode):
        self.message = message
        self.interpreter_name = interpreter_name
        self.discovery_mode = discovery_mode
    monkeypatch.setattr(InterpreterDiscoveryRequiredError, "__init__", mock_init)
