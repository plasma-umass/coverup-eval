# file: httpie/cli/requestitems.py:120-121
# asked: {"lines": [120, 121], "branches": []}
# gained: {"lines": [120, 121], "branches": []}

import pytest
from httpie.cli.requestitems import process_data_item_arg, KeyValueArg

def test_process_data_item_arg():
    # Create a KeyValueArg instance with the required arguments
    arg = KeyValueArg(key='test_key', value='test_value', sep='=', orig='test_key=test_value')
    
    # Call the function with the created argument
    result = process_data_item_arg(arg)
    
    # Assert that the result is the value of the KeyValueArg instance
    assert result == 'test_value'
