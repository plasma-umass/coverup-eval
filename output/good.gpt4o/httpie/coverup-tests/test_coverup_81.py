# file httpie/cli/requestitems.py:134-136
# lines [134, 135, 136]
# branches []

import pytest
from httpie.cli.requestitems import process_data_raw_json_embed_arg, KeyValueArg

def test_process_data_raw_json_embed_arg(mocker):
    # Mock the load_json function to control its output
    mock_load_json = mocker.patch('httpie.cli.requestitems.load_json', return_value={'key': 'value'})

    # Create a KeyValueArg instance
    arg = KeyValueArg(key='test', value='{"key": "value"}', sep='=', orig='test={"key": "value"}')

    # Call the function
    result = process_data_raw_json_embed_arg(arg)

    # Assert that load_json was called with the correct arguments
    mock_load_json.assert_called_once_with(arg, arg.value)

    # Assert the result is as expected
    assert result == {'key': 'value'}
