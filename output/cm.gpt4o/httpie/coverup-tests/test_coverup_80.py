# file httpie/cli/requestitems.py:154-158
# lines [154, 155, 156, 157, 158]
# branches []

import pytest
from httpie.cli.requestitems import load_json, KeyValueArg, ParseError

def test_load_json_valid(mocker):
    mocker.patch('httpie.cli.requestitems.load_json_preserve_order', return_value={"key": "value"})
    arg = KeyValueArg(key="key", value="value", sep="=", orig="test")
    contents = '{"key": "value"}'
    result = load_json(arg, contents)
    assert result == {"key": "value"}

def test_load_json_invalid(mocker):
    mocker.patch('httpie.cli.requestitems.load_json_preserve_order', side_effect=ValueError("Invalid JSON"))
    arg = KeyValueArg(key="key", value="value", sep="=", orig="test")
    contents = 'invalid json'
    with pytest.raises(ParseError) as excinfo:
        load_json(arg, contents)
    assert str(excinfo.value) == '"test": Invalid JSON'
