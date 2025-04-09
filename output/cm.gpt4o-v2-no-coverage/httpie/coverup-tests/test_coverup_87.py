# file: httpie/cli/requestitems.py:134-136
# asked: {"lines": [134, 135, 136], "branches": []}
# gained: {"lines": [134, 135, 136], "branches": []}

import pytest
from httpie.cli.argtypes import KeyValueArg
from httpie.cli.requestitems import process_data_raw_json_embed_arg
from httpie.cli.exceptions import ParseError
from httpie.utils import load_json_preserve_order
import json

def test_process_data_raw_json_embed_arg_valid_json():
    arg = KeyValueArg(key="test", value='{"key": "value"}', sep="=", orig="test={'key': 'value'}")
    result = process_data_raw_json_embed_arg(arg)
    assert result == {"key": "value"}

def test_process_data_raw_json_embed_arg_invalid_json():
    arg = KeyValueArg(key="test", value='{key: value}', sep="=", orig="test={key: value}")
    with pytest.raises(ParseError, match='"test={key: value}": Expecting property name enclosed in double quotes: line 1 column 2 \\(char 1\\)'):
        process_data_raw_json_embed_arg(arg)
