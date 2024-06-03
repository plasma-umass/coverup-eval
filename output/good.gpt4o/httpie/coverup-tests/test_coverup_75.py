# file httpie/cli/requestitems.py:120-121
# lines [120, 121]
# branches []

import pytest
from httpie.cli.requestitems import process_data_item_arg, KeyValueArg

def test_process_data_item_arg():
    # Create a mock KeyValueArg object with all required arguments
    mock_arg = KeyValueArg(key='test_key', value='test_value', sep='=', orig='test_key=test_value')

    # Call the function with the mock object
    result = process_data_item_arg(mock_arg)

    # Assert that the result is as expected
    assert result == 'test_value'
