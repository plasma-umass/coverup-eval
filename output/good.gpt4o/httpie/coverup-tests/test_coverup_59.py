# file httpie/utils.py:14-15
# lines [14, 15]
# branches []

import pytest
import json
from collections import OrderedDict
from httpie.utils import load_json_preserve_order

def test_load_json_preserve_order():
    json_str = '{"b": 1, "a": 2, "c": 3}'
    expected_order = OrderedDict([('b', 1), ('a', 2), ('c', 3)])
    
    result = load_json_preserve_order(json_str)
    
    assert result == expected_order
    assert list(result.keys()) == list(expected_order.keys())
