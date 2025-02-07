# file: httpie/cli/requestitems.py:154-158
# asked: {"lines": [154, 155, 156, 157, 158], "branches": []}
# gained: {"lines": [154, 155, 156, 157, 158], "branches": []}

import pytest
from httpie.cli.argtypes import KeyValueArg
from httpie.cli.exceptions import ParseError
from httpie.utils import load_json_preserve_order
from httpie.cli.requestitems import load_json

def test_load_json_success():
    arg = KeyValueArg(key='test', value='value', sep='=', orig='test=value')
    contents = '{"key": "value"}'
    result = load_json(arg, contents)
    assert result == load_json_preserve_order(contents)

def test_load_json_parse_error():
    arg = KeyValueArg(key='test', value='value', sep='=', orig='test=value')
    contents = '{"key": "value"'  # Malformed JSON
    with pytest.raises(ParseError) as excinfo:
        load_json(arg, contents)
    assert '"test=value": Expecting' in str(excinfo.value)
