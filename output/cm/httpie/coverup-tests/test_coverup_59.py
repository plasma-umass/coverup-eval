# file httpie/utils.py:14-15
# lines [14, 15]
# branches []

import pytest
import json
from collections import OrderedDict
from httpie.utils import load_json_preserve_order

def test_load_json_preserve_order():
    json_str = '{"name": "John", "age": 30, "city": "New York"}'
    expected_dict = OrderedDict([("name", "John"), ("age", 30), ("city", "New York")])
    
    result = load_json_preserve_order(json_str)
    
    assert isinstance(result, OrderedDict), "The result should be an OrderedDict"
    assert result == expected_dict, "The result does not match the expected OrderedDict"
    assert list(result.keys()) == ["name", "age", "city"], "The keys are not in the expected order"
