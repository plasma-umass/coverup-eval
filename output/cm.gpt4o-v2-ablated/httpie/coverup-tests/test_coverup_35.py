# file: httpie/utils.py:14-15
# asked: {"lines": [14, 15], "branches": []}
# gained: {"lines": [14, 15], "branches": []}

import pytest
import json
from collections import OrderedDict
from httpie.utils import load_json_preserve_order

def test_load_json_preserve_order(monkeypatch):
    # Test with a simple JSON string
    json_str = '{"a": 1, "b": 2, "c": 3}'
    result = load_json_preserve_order(json_str)
    assert isinstance(result, OrderedDict)
    assert list(result.keys()) == ['a', 'b', 'c']
    assert result['a'] == 1
    assert result['b'] == 2
    assert result['c'] == 3

    # Test with an empty JSON string
    json_str = '{}'
    result = load_json_preserve_order(json_str)
    assert isinstance(result, OrderedDict)
    assert len(result) == 0

    # Test with nested JSON objects
    json_str = '{"a": {"b": 2}, "c": 3}'
    result = load_json_preserve_order(json_str)
    assert isinstance(result, OrderedDict)
    assert isinstance(result['a'], OrderedDict)
    assert result['a']['b'] == 2
    assert result['c'] == 3

    # Test with invalid JSON string
    json_str = '{"a": 1, "b": 2,'
    with pytest.raises(json.JSONDecodeError):
        load_json_preserve_order(json_str)
