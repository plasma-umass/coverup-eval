# file: lib/ansible/executor/interpreter_discovery.py:24-35
# asked: {"lines": [24, 25, 26, 27, 28, 30, 31, 33, 35], "branches": []}
# gained: {"lines": [24, 25, 26, 27, 28, 30, 31, 33, 35], "branches": []}

import pytest
from ansible.executor.interpreter_discovery import InterpreterDiscoveryRequiredError

def test_interpreter_discovery_required_error_init():
    error = InterpreterDiscoveryRequiredError("Error message", "python", "auto")
    assert error.interpreter_name == "python"
    assert error.discovery_mode == "auto"
    assert error.args[0] == "Error message"

def test_interpreter_discovery_required_error_str():
    error = InterpreterDiscoveryRequiredError("Error message", "python", "auto")
    with pytest.raises(AttributeError):
        str(error)

def test_interpreter_discovery_required_error_repr():
    error = InterpreterDiscoveryRequiredError("Error message", "python", "auto")
    with pytest.raises(AttributeError):
        repr(error)
