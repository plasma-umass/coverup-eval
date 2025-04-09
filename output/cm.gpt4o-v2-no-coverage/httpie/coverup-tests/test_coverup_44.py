# file: httpie/cli/requestitems.py:154-158
# asked: {"lines": [154, 155, 156, 157, 158], "branches": []}
# gained: {"lines": [154, 155, 156, 157, 158], "branches": []}

import pytest
from httpie.cli.argtypes import KeyValueArg
from httpie.cli.exceptions import ParseError
from httpie.utils import load_json_preserve_order
from httpie.cli.requestitems import load_json
from collections import OrderedDict
import json

def test_load_json_success():
    arg = KeyValueArg(key='test', value='{"key": "value"}', sep='=', orig='test={"key": "value"}')
    contents = '{"key": "value"}'
    result = load_json(arg, contents)
    assert result == OrderedDict([('key', 'value')])

def test_load_json_parse_error():
    arg = KeyValueArg(key='test', value='{key: value}', sep='=', orig='test={key: value}')
    contents = '{key: value}'
    with pytest.raises(ParseError) as excinfo:
        load_json(arg, contents)
    assert str(excinfo.value) == '"test={key: value}": Expecting property name enclosed in double quotes: line 1 column 2 (char 1)'

@pytest.fixture(autouse=True)
def cleanup(monkeypatch):
    # Clean up or reset any state if necessary
    yield
    # No specific cleanup required for this test
