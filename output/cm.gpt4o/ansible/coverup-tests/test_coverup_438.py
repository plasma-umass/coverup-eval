# file lib/ansible/module_utils/common/collections.py:74-83
# lines [74, 76, 77, 79, 80, 81, 82, 83]
# branches ['76->77', '76->79']

import pytest
from ansible.module_utils.common.collections import is_iterable

def test_is_iterable_with_string():
    assert not is_iterable("test_string", include_strings=False)
    assert is_iterable("test_string", include_strings=True)

def test_is_iterable_with_non_iterable():
    assert not is_iterable(123, include_strings=False)
    assert not is_iterable(123, include_strings=True)

def test_is_iterable_with_iterable():
    assert is_iterable([1, 2, 3], include_strings=False)
    assert is_iterable((1, 2, 3), include_strings=False)
    assert is_iterable({1, 2, 3}, include_strings=False)
    assert is_iterable({'a': 1, 'b': 2}, include_strings=False)

@pytest.fixture(autouse=True)
def cleanup():
    yield
    # Add any necessary cleanup code here
