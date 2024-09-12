# file: httpie/utils.py:18-19
# asked: {"lines": [18, 19], "branches": []}
# gained: {"lines": [18, 19], "branches": []}

import pytest
from httpie.utils import repr_dict
from pprint import pformat

def test_repr_dict_empty():
    d = {}
    result = repr_dict(d)
    assert result == pformat(d)
    assert result == '{}'

def test_repr_dict_non_empty():
    d = {'key': 'value', 'another_key': 123}
    result = repr_dict(d)
    assert result == pformat(d)
    assert result == "{'another_key': 123, 'key': 'value'}"
