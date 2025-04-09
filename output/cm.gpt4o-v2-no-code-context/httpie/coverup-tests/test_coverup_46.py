# file: httpie/utils.py:14-15
# asked: {"lines": [14, 15], "branches": []}
# gained: {"lines": [14, 15], "branches": []}

import pytest
import json
from collections import OrderedDict
from httpie.utils import load_json_preserve_order

def test_load_json_preserve_order(monkeypatch):
    json_string = '{"a": 1, "b": 2, "c": 3}'
    expected_output = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
    
    result = load_json_preserve_order(json_string)
    
    assert result == expected_output
    assert isinstance(result, OrderedDict)
