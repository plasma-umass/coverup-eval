# file: httpie/utils.py:14-15
# asked: {"lines": [14, 15], "branches": []}
# gained: {"lines": [14, 15], "branches": []}

import pytest
import json
from collections import OrderedDict
from httpie.utils import load_json_preserve_order

def test_load_json_preserve_order():
    json_str = '{"a": 1, "b": 2, "c": 3}'
    expected_result = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
    
    result = load_json_preserve_order(json_str)
    
    assert result == expected_result
    assert isinstance(result, OrderedDict)
