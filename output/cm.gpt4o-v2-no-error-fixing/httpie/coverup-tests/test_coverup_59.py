# file: httpie/cli/requestitems.py:120-121
# asked: {"lines": [120, 121], "branches": []}
# gained: {"lines": [120, 121], "branches": []}

import pytest
from httpie.cli.argtypes import KeyValueArg
from httpie.cli.requestitems import process_data_item_arg

def test_process_data_item_arg():
    # Create a KeyValueArg instance
    arg = KeyValueArg(key='test_key', value='test_value', sep='=', orig='test_key=test_value')
    
    # Call the function with the KeyValueArg instance
    result = process_data_item_arg(arg)
    
    # Assert that the result is the value of the KeyValueArg instance
    assert result == 'test_value'
