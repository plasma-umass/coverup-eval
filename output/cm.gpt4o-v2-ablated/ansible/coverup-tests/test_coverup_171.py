# file: lib/ansible/module_utils/common/collections.py:74-83
# asked: {"lines": [74, 76, 77, 79, 80, 81, 82, 83], "branches": [[76, 77], [76, 79]]}
# gained: {"lines": [74, 76, 77, 79, 80, 81, 82, 83], "branches": [[76, 77], [76, 79]]}

import pytest
from ansible.module_utils.common.collections import is_iterable

def test_is_iterable_with_list():
    assert is_iterable([1, 2, 3]) is True

def test_is_iterable_with_tuple():
    assert is_iterable((1, 2, 3)) is True

def test_is_iterable_with_dict():
    assert is_iterable({'a': 1, 'b': 2}) is True

def test_is_iterable_with_set():
    assert is_iterable({1, 2, 3}) is True

def test_is_iterable_with_string_include_strings_false():
    assert is_iterable("string", include_strings=False) is False

def test_is_iterable_with_string_include_strings_true():
    assert is_iterable("string", include_strings=True) is True

def test_is_iterable_with_int():
    assert is_iterable(123) is False

def test_is_iterable_with_none():
    assert is_iterable(None) is False

def test_is_iterable_with_generator():
    def gen():
        yield 1
    assert is_iterable(gen()) is True
