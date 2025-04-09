# file: lib/ansible/utils/unsafe_proxy.py:105-106
# asked: {"lines": [106], "branches": []}
# gained: {"lines": [106], "branches": []}

import pytest
from ansible.utils.unsafe_proxy import _wrap_dict, wrap_var

def test_wrap_dict_with_empty_dict():
    result = _wrap_dict({})
    assert result == {}

def test_wrap_dict_with_non_empty_dict():
    input_dict = {'key1': 'value1', 'key2': 'value2'}
    result = _wrap_dict(input_dict)
    assert result == {wrap_var('key1'): wrap_var('value1'), wrap_var('key2'): wrap_var('value2')}
