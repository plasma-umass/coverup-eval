# file: pytutils/lazy/lazy_import.py:189-191
# asked: {"lines": [190, 191], "branches": []}
# gained: {"lines": [190, 191], "branches": []}

import pytest
from unittest.mock import Mock, patch

# Assuming the ScopeReplacer class is imported from pytutils.lazy.lazy_import
from pytutils.lazy.lazy_import import ScopeReplacer

@pytest.fixture
def mock_resolve():
    with patch.object(ScopeReplacer, '_resolve', return_value=Mock()) as mock_resolve:
        yield mock_resolve

def test_scope_replacer_call(mock_resolve):
    # Create a dictionary to act as the scope
    scope = {}
    factory = Mock()
    name = 'test_name'
    replacer = ScopeReplacer(scope, factory, name)
    
    # Mock the return value of the _resolve method
    mock_obj = Mock()
    mock_resolve.return_value = mock_obj
    
    # Call the replacer with some arguments
    args = (1, 2, 3)
    kwargs = {'a': 4, 'b': 5}
    replacer(*args, **kwargs)
    
    # Assert that _resolve was called
    mock_resolve.assert_called_once()
    
    # Assert that the returned object was called with the correct arguments
    mock_obj.assert_called_once_with(*args, **kwargs)
