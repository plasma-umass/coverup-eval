# file: httpie/cli/requestitems.py:128-131
# asked: {"lines": [128, 129, 130, 131], "branches": []}
# gained: {"lines": [128, 129, 130, 131], "branches": []}

import pytest
from unittest.mock import patch, mock_open
from httpie.cli.argtypes import KeyValueArg
from httpie.cli.requestitems import process_data_embed_raw_json_file_arg

@pytest.fixture
def key_value_arg():
    return KeyValueArg(key='test', value='{"key": "value"}', sep='=', orig='test={"key": "value"}')

@patch('httpie.cli.requestitems.load_text_file', return_value='{"key": "value"}')
@patch('httpie.cli.requestitems.load_json', return_value={"key": "value"})
def test_process_data_embed_raw_json_file_arg(mock_load_json, mock_load_text_file, key_value_arg):
    result = process_data_embed_raw_json_file_arg(key_value_arg)
    mock_load_text_file.assert_called_once_with(key_value_arg)
    mock_load_json.assert_called_once_with(key_value_arg, '{"key": "value"}')
    assert result == {"key": "value"}
