# file: lib/ansible/module_utils/connection.py:112-117
# asked: {"lines": [112, 114, 115, 116, 117], "branches": [[116, 0], [116, 117]]}
# gained: {"lines": [112, 114, 115, 116, 117], "branches": [[116, 0], [116, 117]]}

import pytest
from ansible.module_utils.connection import ConnectionError

def test_connection_error_with_kwargs():
    # Create an instance of ConnectionError with additional keyword arguments
    error = ConnectionError("Test message", code=500, reason="Server Error")
    
    # Assertions to verify that the attributes are set correctly
    assert error.code == 500
    assert error.reason == "Server Error"
    assert str(error) == "Test message"

def test_connection_error_without_kwargs():
    # Create an instance of ConnectionError without additional keyword arguments
    error = ConnectionError("Test message")
    
    # Assertions to verify that no additional attributes are set
    assert not hasattr(error, 'code')
    assert not hasattr(error, 'reason')
    assert str(error) == "Test message"
