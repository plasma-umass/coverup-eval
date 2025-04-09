# file thefuck/shells/generic.py:52-54
# lines [52, 53, 54]
# branches []

import pytest
from unittest.mock import patch, MagicMock
from thefuck.shells.generic import Generic

def test_get_history(mocker):
    # Mock the _get_history_lines method to return a specific value
    mocker.patch.object(Generic, '_get_history_lines', return_value=['line1', 'line2', 'line3'])
    
    # Create an instance of the Generic class
    generic = Generic()
    
    # Call the get_history method
    history = generic.get_history()
    
    # Assert that the history is as expected
    assert history == ['line1', 'line2', 'line3']
    
    # Clean up by resetting the memoize cache
    if hasattr(generic.get_history, 'cache_clear'):
        generic.get_history.cache_clear()
