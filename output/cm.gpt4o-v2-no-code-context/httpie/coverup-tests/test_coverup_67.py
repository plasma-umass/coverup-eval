# file: httpie/cli/requestitems.py:128-131
# asked: {"lines": [128, 129, 130, 131], "branches": []}
# gained: {"lines": [128, 129, 130, 131], "branches": []}

import pytest
from httpie.cli.requestitems import process_data_embed_raw_json_file_arg, KeyValueArg

@pytest.fixture
def mock_load_text_file(mocker):
    return mocker.patch('httpie.cli.requestitems.load_text_file')

@pytest.fixture
def mock_load_json(mocker):
    return mocker.patch('httpie.cli.requestitems.load_json')

def test_process_data_embed_raw_json_file_arg(mock_load_text_file, mock_load_json):
    # Arrange
    arg = KeyValueArg(key='test', value='test.json', sep='=', orig='test=test.json')
    mock_load_text_file.return_value = '{"key": "value"}'
    mock_load_json.return_value = {"key": "value"}

    # Act
    result = process_data_embed_raw_json_file_arg(arg)

    # Assert
    mock_load_text_file.assert_called_once_with(arg)
    mock_load_json.assert_called_once_with(arg, '{"key": "value"}')
    assert result == {"key": "value"}
