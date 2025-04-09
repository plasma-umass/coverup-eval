# file: httpie/cli/requestitems.py:128-131
# asked: {"lines": [128, 129, 130, 131], "branches": []}
# gained: {"lines": [128, 129, 130, 131], "branches": []}

import pytest
from httpie.cli.argtypes import KeyValueArg
from httpie.cli.requestitems import process_data_embed_raw_json_file_arg
import json

def load_text_file(arg):
    # Mock implementation of load_text_file
    return '{"key": "value"}'

def load_json(arg, contents):
    # Mock implementation of load_json
    return json.loads(contents)

def test_process_data_embed_raw_json_file_arg(monkeypatch):
    # Arrange
    arg = KeyValueArg(key='test', value='{"key": "value"}', sep='=', orig='test={"key": "value"}')
    
    # Mock the load_text_file and load_json functions
    monkeypatch.setattr('httpie.cli.requestitems.load_text_file', load_text_file)
    monkeypatch.setattr('httpie.cli.requestitems.load_json', load_json)
    
    # Act
    result = process_data_embed_raw_json_file_arg(arg)
    
    # Assert
    assert result == {"key": "value"}
