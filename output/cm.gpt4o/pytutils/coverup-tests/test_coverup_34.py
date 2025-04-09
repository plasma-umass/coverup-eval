# file pytutils/lazy/lazy_import.py:189-191
# lines [189, 190, 191]
# branches []

import pytest
from unittest.mock import Mock, patch

# Assuming the ScopeReplacer class is imported from pytutils.lazy.lazy_import
from pytutils.lazy.lazy_import import ScopeReplacer

@pytest.fixture
def mock_resolve():
    with patch.object(ScopeReplacer, '_resolve', return_value=Mock()) as mock_resolve:
        yield mock_resolve

def test_scope_replacer_call(mock_resolve):
    # Mock the required arguments for ScopeReplacer
    mock_scope = {}
    mock_factory = Mock()
    mock_name = 'test_name'
    
    # Create an instance of ScopeReplacer with mocked arguments
    replacer = ScopeReplacer(mock_scope, mock_factory, mock_name)
    
    # Mock the object returned by _resolve
    mock_obj = mock_resolve.return_value
    mock_obj.return_value = 'expected_result'
    
    # Call the replacer with some arguments
    result = replacer('arg1', 'arg2', kwarg1='value1')
    
    # Assert that the _resolve method was called
    mock_resolve.assert_called_once()
    
    # Assert that the returned object was called with the correct arguments
    mock_obj.assert_called_once_with('arg1', 'arg2', kwarg1='value1')
    
    # Assert the result is as expected
    assert result == 'expected_result'
