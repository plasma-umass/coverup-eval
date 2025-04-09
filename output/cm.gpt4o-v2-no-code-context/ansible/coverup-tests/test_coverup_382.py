# file: lib/ansible/module_utils/common/collections.py:74-83
# asked: {"lines": [74, 76, 77, 79, 80, 81, 82, 83], "branches": [[76, 77], [76, 79]]}
# gained: {"lines": [74, 76, 77, 79, 80, 81, 82, 83], "branches": [[76, 77], [76, 79]]}

import pytest
from ansible.module_utils.common.collections import is_iterable

def test_is_iterable_with_string():
    assert not is_iterable("test_string")

def test_is_iterable_with_string_include_strings():
    assert is_iterable("test_string", include_strings=True)

def test_is_iterable_with_list():
    assert is_iterable([1, 2, 3])

def test_is_iterable_with_non_iterable():
    assert not is_iterable(42)

def test_is_iterable_with_dict():
    assert is_iterable({"key": "value"})

def test_is_iterable_with_set():
    assert is_iterable({1, 2, 3})

def test_is_iterable_with_tuple():
    assert is_iterable((1, 2, 3))

def test_is_iterable_with_generator():
    def gen():
        yield 1
    assert is_iterable(gen())
