# file: lib/ansible/plugins/filter/mathstuff.py:100-106
# asked: {"lines": [103], "branches": [[102, 103]]}
# gained: {"lines": [103], "branches": [[102, 103]]}

import pytest
from ansible.plugins.filter.mathstuff import difference
from jinja2 import Environment
from collections.abc import Hashable

@pytest.fixture
def environment():
    return Environment()

def test_difference_with_hashable_sets(environment):
    a = frozenset([1, 2, 3])
    b = frozenset([2, 3, 4])
    result = difference(environment, a, b)
    assert result == frozenset([1])

def test_difference_with_non_hashable_lists(environment):
    a = [1, 2, 3]
    b = [2, 3, 4]
    result = difference(environment, a, b)
    assert result == [1]

def test_difference_with_mixed_types(environment):
    a = {1, 2, 3}
    b = [2, 3, 4]
    result = difference(environment, a, b)
    assert set(result) == {1}

def test_difference_with_empty_sets(environment):
    a = set()
    b = {2, 3, 4}
    result = difference(environment, a, b)
    assert set(result) == set()

def test_difference_with_empty_lists(environment):
    a = []
    b = [2, 3, 4]
    result = difference(environment, a, b)
    assert result == []
