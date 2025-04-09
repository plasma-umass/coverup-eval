# file lib/ansible/module_utils/connection.py:112-117
# lines [112, 114, 115, 116, 117]
# branches ['116->exit', '116->117']

import pytest
from ansible.module_utils.connection import ConnectionError

def test_connection_error_initialization():
    # Test initialization with message only
    error = ConnectionError("Test message")
    assert str(error) == "Test message"
    
    # Test initialization with message and additional attributes
    error = ConnectionError("Test message with kwargs", code=500, reason="Internal Server Error")
    assert str(error) == "Test message with kwargs"
    assert error.code == 500
    assert error.reason == "Internal Server Error"

@pytest.fixture(autouse=True)
def cleanup():
    yield
    # Perform any necessary cleanup here
