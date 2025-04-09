# file httpie/cli/requestitems.py:134-136
# lines [134, 135, 136]
# branches []

import pytest
from httpie.cli.requestitems import KeyValueArg, process_data_raw_json_embed_arg
from httpie.cli.exceptions import ParseError

@pytest.fixture
def mock_load_json(mocker):
    return mocker.patch('httpie.cli.requestitems.load_json', return_value={'key': 'value'})

def test_process_data_raw_json_embed_arg(mock_load_json):
    # Given a KeyValueArg with a JSON value
    arg = KeyValueArg(key='key', value='{"key": "value"}', sep=':', orig='key:{"key": "value"}')

    # When process_data_raw_json_embed_arg is called
    result = process_data_raw_json_embed_arg(arg)

    # Then the result should be the JSON loaded from the value
    assert result == {'key': 'value'}
    mock_load_json.assert_called_once_with(arg, arg.value)

def test_process_data_raw_json_embed_arg_invalid_json():
    # Given a KeyValueArg with an invalid JSON value
    arg = KeyValueArg(key='key', value='invalid_json', sep=':', orig='key:invalid_json')

    # When process_data_raw_json_embed_arg is called with invalid JSON
    # Then a ParseError should be raised
    with pytest.raises(ParseError):
        process_data_raw_json_embed_arg(arg)
