# file: httpie/utils.py:18-19
# asked: {"lines": [18, 19], "branches": []}
# gained: {"lines": [18, 19], "branches": []}

import pytest
from httpie.utils import repr_dict

def test_repr_dict():
    test_dict = {'key1': 'value1', 'key2': 'value2'}
    expected_output = "{'key1': 'value1', 'key2': 'value2'}"
    
    assert repr_dict(test_dict) == expected_output
