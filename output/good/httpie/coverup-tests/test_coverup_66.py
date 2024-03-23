# file httpie/cli/requestitems.py:154-158
# lines [154, 155, 156, 157, 158]
# branches []

import pytest
from httpie.cli.requestitems import KeyValueArg, ParseError, load_json

def test_load_json_with_invalid_json():
    invalid_json_content = "{'invalid': 'json'}"  # Invalid JSON due to single quotes
    key_value_arg = KeyValueArg('field:=invalid_json_content', ':=', 'invalid_json_content', 'field:=invalid_json_content')

    with pytest.raises(ParseError) as exc_info:
        load_json(key_value_arg, invalid_json_content)

    assert '"field:=invalid_json_content": Expecting property name enclosed in double quotes: line 1 column 2 (char 1)' in str(exc_info.value)

def test_load_json_with_valid_json():
    valid_json_content = '{"valid": "json"}'
    key_value_arg = KeyValueArg('field:=valid_json_content', ':=', 'valid_json_content', 'field:=valid_json_content')

    result = load_json(key_value_arg, valid_json_content)

    assert result == {"valid": "json"}
