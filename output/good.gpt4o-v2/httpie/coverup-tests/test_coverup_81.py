# file: httpie/cli/requestitems.py:120-121
# asked: {"lines": [120, 121], "branches": []}
# gained: {"lines": [120, 121], "branches": []}

import pytest
from httpie.cli.argtypes import KeyValueArg
from httpie.cli.requestitems import process_data_item_arg

def test_process_data_item_arg():
    # Create a KeyValueArg instance with a value
    arg = KeyValueArg(key="test_key", value="test_value", sep="=", orig="test_key=test_value")
    
    # Call the function and assert the return value
    result = process_data_item_arg(arg)
    assert result == "test_value"

    # Create a KeyValueArg instance with a None value
    arg_none = KeyValueArg(key="test_key", value=None, sep="=", orig="test_key=")
    
    # Call the function and assert the return value is None
    result_none = process_data_item_arg(arg_none)
    assert result_none is None
