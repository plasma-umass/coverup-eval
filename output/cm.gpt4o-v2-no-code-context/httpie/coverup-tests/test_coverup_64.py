# file: httpie/cli/requestitems.py:101-102
# asked: {"lines": [101, 102], "branches": []}
# gained: {"lines": [101, 102], "branches": []}

import pytest
from httpie.cli.requestitems import process_query_param_arg, KeyValueArg

def test_process_query_param_arg():
    # Create a KeyValueArg instance with a specific value
    arg = KeyValueArg(key='test_key', value='test_value', sep='=', orig='test_key=test_value')
    
    # Call the function with the KeyValueArg instance
    result = process_query_param_arg(arg)
    
    # Assert that the result is the value of the KeyValueArg instance
    assert result == 'test_value'
