# file lib/ansible/plugins/filter/mathstuff.py:119-125
# lines [119, 120, 121, 122, 124, 125]
# branches ['121->122', '121->124']

import pytest
from ansible.plugins.filter.mathstuff import union
from jinja2 import Environment
from collections.abc import Hashable

@pytest.fixture
def environment():
    return Environment()

def test_union_with_hashable(environment):
    a = frozenset([1, 2, 3])
    b = frozenset([3, 4, 5])
    result = union(environment, a, b)
    assert result == {1, 2, 3, 4, 5}

def test_union_with_non_hashable(environment, mocker):
    mocker.patch('ansible.plugins.filter.mathstuff.unique', return_value=[1, 2, 3, 4, 5])
    a = [1, 2, 3]
    b = [3, 4, 5]
    result = union(environment, a, b)
    assert result == [1, 2, 3, 4, 5]
