# file lib/ansible/module_utils/connection.py:112-117
# lines [112, 114, 115, 116, 117]
# branches ['116->exit', '116->117']

import pytest
from ansible.module_utils.connection import ConnectionError
from ansible.module_utils.six import iteritems

def test_connection_error_initialization():
    # Create a ConnectionError instance with additional kwargs
    error = ConnectionError("Test error", code=404, url="http://example.com")

    # Assert that the message has been set correctly
    assert str(error) == "Test error"

    # Assert that the additional kwargs have been set as attributes
    assert error.code == 404
    assert error.url == "http://example.com"

def test_connection_error_without_kwargs():
    # Create a ConnectionError instance without additional kwargs
    error = ConnectionError("Test error")

    # Assert that the message has been set correctly
    assert str(error) == "Test error"

    # Assert that no additional attributes are set
    with pytest.raises(AttributeError):
        getattr(error, 'code')
    with pytest.raises(AttributeError):
        getattr(error, 'url')

def test_connection_error_with_empty_kwargs():
    # Create a ConnectionError instance with empty kwargs
    error = ConnectionError("Test error", **{})

    # Assert that the message has been set correctly
    assert str(error) == "Test error"

    # Assert that no additional attributes are set
    with pytest.raises(AttributeError):
        getattr(error, 'code')
    with pytest.raises(AttributeError):
        getattr(error, 'url')

# Ensure that the test does not affect other tests by not having any side effects
