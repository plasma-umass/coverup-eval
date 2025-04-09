# file httpie/cli/requestitems.py:124-125
# lines [124, 125]
# branches []

import pytest
from httpie.cli.requestitems import process_data_embed_file_contents_arg, KeyValueArg
from unittest.mock import patch

def test_process_data_embed_file_contents_arg(mocker):
    # Mock the load_text_file function
    mock_load_text_file = mocker.patch('httpie.cli.requestitems.load_text_file', return_value='file content')

    # Create a KeyValueArg instance with all required arguments
    arg = KeyValueArg(key='test', value='test.txt', sep='=', orig='test=test.txt')

    # Call the function
    result = process_data_embed_file_contents_arg(arg)

    # Assert that load_text_file was called with the correct argument
    mock_load_text_file.assert_called_once_with(arg)

    # Assert the result is as expected
    assert result == 'file content'
