# file lib/ansible/plugins/filter/core.py:220-237
# lines [220, 221, 222, 223, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 237]
# branches ['222->223', '222->225', '226->227', '226->232', '227->228', '227->229', '229->230', '229->231', '232->233', '232->237', '233->234', '233->235']

import pytest
from ansible.errors import AnsibleFilterError
from ansible.plugins.filter.core import rand
from unittest.mock import patch

def test_rand_with_integer_end():
    result = rand(None, 10)
    assert 0 <= result < 10

def test_rand_with_integer_end_and_start():
    result = rand(None, 10, start=5)
    assert 5 <= result < 10

def test_rand_with_integer_end_start_and_step():
    result = rand(None, 10, start=2, step=2)
    assert result in range(2, 10, 2)

def test_rand_with_seed():
    result1 = rand(None, 10, seed=42)
    result2 = rand(None, 10, seed=42)
    assert result1 == result2

def test_rand_with_iterable_end():
    result = rand(None, [1, 2, 3, 4])
    assert result in [1, 2, 3, 4]

def test_rand_with_iterable_end_raises_error_with_start():
    with pytest.raises(AnsibleFilterError, match='start and step can only be used with integer values'):
        rand(None, [1, 2, 3, 4], start=1)

def test_rand_with_iterable_end_raises_error_with_step():
    with pytest.raises(AnsibleFilterError, match='start and step can only be used with integer values'):
        rand(None, [1, 2, 3, 4], step=1)

def test_rand_raises_error_with_invalid_end():
    with pytest.raises(AnsibleFilterError, match='random can only be used on sequences and integers'):
        rand(None, object())
