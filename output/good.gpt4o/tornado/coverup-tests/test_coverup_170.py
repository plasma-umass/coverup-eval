# file tornado/options.py:167-168
# lines [167, 168]
# branches []

import pytest
from unittest import mock

# Assuming the OptionParser class is defined in tornado.options
from tornado.options import OptionParser

def test_option_parser_getitem():
    parser = OptionParser()
    
    # Mock the __getattr__ method to return a specific value
    with mock.patch.object(OptionParser, '__getattr__', return_value='mocked_value') as mock_getattr:
        result = parser['test_option']
        
        # Verify that __getattr__ was called with the correct argument
        mock_getattr.assert_called_once_with('test_option')
        
        # Verify the result is as expected
        assert result == 'mocked_value'
