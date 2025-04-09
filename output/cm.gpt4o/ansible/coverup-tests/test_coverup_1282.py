# file lib/ansible/plugins/filter/mathstuff.py:91-97
# lines [94]
# branches ['93->94']

import pytest
from ansible.plugins.filter.mathstuff import intersect
from jinja2 import Environment
from collections.abc import Hashable

@pytest.fixture
def environment():
    return Environment()

def test_intersect_hashable(environment):
    a = {1, 2, 3}
    b = {2, 3, 4}
    result = intersect(environment, a, b)
    assert set(result) == {2, 3}

def test_intersect_non_hashable(environment, mocker):
    mocker.patch('ansible.plugins.filter.mathstuff.unique', return_value=[2, 3])
    a = [1, 2, 3]
    b = [2, 3, 4]
    result = intersect(environment, a, b)
    assert result == [2, 3]

def test_intersect_string(environment):
    a = "abc"
    b = "bcd"
    result = intersect(environment, a, b)
    assert set(result) == {'b', 'c'}
