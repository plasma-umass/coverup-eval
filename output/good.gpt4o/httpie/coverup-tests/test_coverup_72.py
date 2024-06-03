# file httpie/cli/requestitems.py:101-102
# lines [101, 102]
# branches []

import pytest
from httpie.cli.requestitems import process_query_param_arg
from httpie.cli.argtypes import KeyValueArg

def test_process_query_param_arg():
    # Create a mock KeyValueArg object with all required arguments
    mock_arg = KeyValueArg(key='test_key', value='test_value', sep='=', orig='test_key=test_value')
    
    # Call the function with the mock object
    result = process_query_param_arg(mock_arg)
    
    # Assert that the result is as expected
    assert result == 'test_value'
