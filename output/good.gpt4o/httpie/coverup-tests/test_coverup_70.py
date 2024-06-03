# file httpie/cli/requestitems.py:128-131
# lines [128, 129, 130, 131]
# branches []

import pytest
from httpie.cli.requestitems import process_data_embed_raw_json_file_arg
from httpie.cli.argtypes import KeyValueArg
from unittest.mock import patch

def test_process_data_embed_raw_json_file_arg(mocker):
    # Mock the load_text_file and load_json functions
    mock_load_text_file = mocker.patch('httpie.cli.requestitems.load_text_file')
    mock_load_json = mocker.patch('httpie.cli.requestitems.load_json')

    # Define the test argument and mock return values
    test_arg = KeyValueArg(key='test', value='test.json', sep='=', orig='test=test.json')
    mock_load_text_file.return_value = '{"key": "value"}'
    mock_load_json.return_value = {"key": "value"}

    # Call the function with the test argument
    result = process_data_embed_raw_json_file_arg(test_arg)

    # Assertions to verify the function behavior
    mock_load_text_file.assert_called_once_with(test_arg)
    mock_load_json.assert_called_once_with(test_arg, '{"key": "value"}')
    assert result == {"key": "value"}
