# file: httpie/cli/requestitems.py:134-136
# asked: {"lines": [134, 135, 136], "branches": []}
# gained: {"lines": [134, 135, 136], "branches": []}

import pytest
from httpie.cli.requestitems import process_data_raw_json_embed_arg, KeyValueArg

def test_process_data_raw_json_embed_arg(monkeypatch):
    class MockKeyValueArg:
        def __init__(self, key, value):
            self.key = key
            self.value = value

    def mock_load_json(arg, value):
        assert arg.key == 'test_key'
        assert value == '{"test": "value"}'
        return {"test": "value"}

    monkeypatch.setattr('httpie.cli.requestitems.load_json', mock_load_json)

    arg = MockKeyValueArg('test_key', '{"test": "value"}')
    result = process_data_raw_json_embed_arg(arg)
    assert result == {"test": "value"}
