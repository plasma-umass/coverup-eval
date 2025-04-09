# file: httpie/utils.py:18-19
# asked: {"lines": [18, 19], "branches": []}
# gained: {"lines": [18, 19], "branches": []}

import pytest
from httpie.utils import repr_dict
from unittest.mock import patch
from pprint import pformat

def test_repr_dict():
    test_dict = {'key': 'value'}
    expected_output = pformat(test_dict)
    assert repr_dict(test_dict) == expected_output

def test_repr_dict_empty():
    test_dict = {}
    expected_output = pformat(test_dict)
    assert repr_dict(test_dict) == expected_output
