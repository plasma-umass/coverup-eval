# file: lib/ansible/module_utils/connection.py:112-117
# asked: {"lines": [112, 114, 115, 116, 117], "branches": [[116, 0], [116, 117]]}
# gained: {"lines": [112, 114, 115, 116, 117], "branches": [[116, 0], [116, 117]]}

import pytest
from ansible.module_utils.connection import ConnectionError
from ansible.module_utils.six import iteritems

def test_connection_error_initialization():
    # Test initialization with only a message
    error = ConnectionError("Test message")
    assert str(error) == "Test message"
    
    # Test initialization with message and additional keyword arguments
    error = ConnectionError("Test message", code=500, reason="Server Error")
    assert str(error) == "Test message"
    assert error.code == 500
    assert error.reason == "Server Error"

def test_connection_error_no_kwargs():
    # Test initialization with no kwargs
    error = ConnectionError("No kwargs")
    assert str(error) == "No kwargs"
    assert not hasattr(error, 'code')
    assert not hasattr(error, 'reason')

def test_connection_error_empty_kwargs():
    # Test initialization with empty kwargs
    error = ConnectionError("Empty kwargs", **{})
    assert str(error) == "Empty kwargs"
    assert not hasattr(error, 'code')
    assert not hasattr(error, 'reason')
