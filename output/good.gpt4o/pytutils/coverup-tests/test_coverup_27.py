# file pytutils/lazy/lazy_import.py:181-183
# lines [181, 182, 183]
# branches []

import pytest
from unittest.mock import MagicMock

# Assuming the ScopeReplacer class is imported from pytutils.lazy.lazy_import
from pytutils.lazy.lazy_import import ScopeReplacer

def test_scope_replacer_getattribute(mocker):
    # Mock the _resolve method to return a mock object
    mock_resolve = MagicMock()
    mock_obj = MagicMock()
    mock_resolve.return_value = mock_obj

    # Create a dummy class to inherit from ScopeReplacer to bypass the __init__ arguments
    class DummyScopeReplacer(ScopeReplacer):
        def __init__(self):
            pass

    # Create an instance of DummyScopeReplacer and set the _resolve attribute
    replacer = DummyScopeReplacer()
    object.__setattr__(replacer, '_resolve', mock_resolve)

    # Access an attribute to trigger __getattribute__
    mock_obj.some_attribute = 'test_value'
    result = replacer.some_attribute

    # Assertions to verify the behavior
    mock_resolve.assert_called_once()
    assert result == 'test_value'

    # Clean up
    del replacer
