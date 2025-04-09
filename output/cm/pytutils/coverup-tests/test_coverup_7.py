# file pytutils/lazy/lazy_import.py:136-149
# lines [136, 145, 146, 147, 148, 149]
# branches []

import pytest
from unittest.mock import Mock

# Assuming the ScopeReplacer class is in a file named lazy_import.py
from pytutils.lazy.lazy_import import ScopeReplacer

def test_scope_replacer():
    mock_scope = {}
    mock_factory = Mock()
    name = 'test_name'

    # Create an instance of ScopeReplacer
    replacer = ScopeReplacer(mock_scope, mock_factory, name)

    # Assert that the replacer is in the scope with the correct name
    assert mock_scope[name] is replacer

    # Access the attribute to trigger the factory call
    _ = replacer.__dict__

    # Assert that the factory was called with the correct arguments
    mock_factory.assert_called_once_with(replacer, mock_scope, name)

    # Assert that the real object is now in the scope
    assert mock_scope[name] is not replacer
    assert mock_scope[name] == mock_factory.return_value

    # Clean up the mock scope
    del mock_scope[name]

@pytest.fixture(autouse=True)
def clean_scope_replacer():
    # Setup code before each test function
    yield
    # Cleanup code after each test function
    # No cleanup needed for this test as the scope is a local dictionary

# Run the test function
def test_scope_replacer_execution():
    test_scope_replacer()
