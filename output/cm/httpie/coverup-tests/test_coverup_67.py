# file httpie/cli/requestitems.py:124-125
# lines [124, 125]
# branches []

import pytest
from httpie.cli.requestitems import KeyValueArg, process_data_embed_file_contents_arg
from unittest.mock import mock_open, patch

# Assuming that the load_text_file function is defined elsewhere in the module
# and that it reads the contents of a file whose path is given by the value of the KeyValueArg.

@pytest.fixture
def mock_load_text_file(mocker):
    mock = mocker.patch('httpie.cli.requestitems.load_text_file', return_value='file contents')
    return mock

def test_process_data_embed_file_contents_arg(mock_load_text_file):
    # Create a KeyValueArg instance with a dummy file path
    arg = KeyValueArg(key='key', value='dummy_file_path', sep='=', orig='key=dummy_file_path')
    
    # Call the function under test
    result = process_data_embed_file_contents_arg(arg)
    
    # Assert that the load_text_file function was called with the correct argument
    mock_load_text_file.assert_called_once_with(arg)
    
    # Assert that the result is the content that the mock is set up to return
    assert result == 'file contents'
