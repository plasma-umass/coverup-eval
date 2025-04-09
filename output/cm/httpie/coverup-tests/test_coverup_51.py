# file httpie/utils.py:18-19
# lines [18, 19]
# branches []

import pytest
from httpie.utils import repr_dict
from pprint import pformat

def test_repr_dict():
    test_dict = {'key1': 'value1', 'key2': 'value2'}
    expected_repr = pformat(test_dict)
    assert repr_dict(test_dict) == expected_repr
