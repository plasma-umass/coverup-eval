# file: lib/ansible/module_utils/common/collections.py:74-83
# asked: {"lines": [74, 76, 77, 79, 80, 81, 82, 83], "branches": [[76, 77], [76, 79]]}
# gained: {"lines": [74, 76, 77, 79, 80, 81, 82, 83], "branches": [[76, 77], [76, 79]]}

import pytest
from ansible.module_utils.common.collections import is_iterable
from ansible.module_utils.six import binary_type, text_type

def test_is_iterable_with_string():
    assert not is_iterable("string", include_strings=False)
    assert is_iterable("string", include_strings=True)

def test_is_iterable_with_list():
    assert is_iterable([1, 2, 3], include_strings=False)
    assert is_iterable([1, 2, 3], include_strings=True)

def test_is_iterable_with_non_iterable():
    assert not is_iterable(42, include_strings=False)
    assert not is_iterable(42, include_strings=True)

def test_is_iterable_with_custom_iterable():
    class CustomIterable:
        def __iter__(self):
            return iter([1, 2, 3])
    
    assert is_iterable(CustomIterable(), include_strings=False)
    assert is_iterable(CustomIterable(), include_strings=True)

def test_is_iterable_with_custom_non_iterable():
    class CustomNonIterable:
        pass
    
    assert not is_iterable(CustomNonIterable(), include_strings=False)
    assert not is_iterable(CustomNonIterable(), include_strings=True)
