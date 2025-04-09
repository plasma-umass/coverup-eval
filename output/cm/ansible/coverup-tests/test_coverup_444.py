# file lib/ansible/module_utils/common/collections.py:74-83
# lines [74, 76, 77, 79, 80, 81, 82, 83]
# branches ['76->77', '76->79']

import pytest
from ansible.module_utils.common.collections import is_iterable

def test_is_iterable_with_non_string():
    assert is_iterable([1, 2, 3]) == True, "List should be identified as iterable"

def test_is_iterable_with_string_not_included():
    assert is_iterable("abc", include_strings=False) == False, "String should not be identified as iterable when include_strings is False"

def test_is_iterable_with_string_included():
    assert is_iterable("abc", include_strings=True) == True, "String should be identified as iterable when include_strings is True"

def test_is_iterable_with_non_iterable():
    assert is_iterable(123) == False, "Integer should not be identified as iterable"
