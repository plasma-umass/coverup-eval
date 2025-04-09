# file lib/ansible/plugins/filter/mathstuff.py:91-97
# lines [91, 92, 93, 94, 96, 97]
# branches ['93->94', '93->96']

import pytest
from ansible.plugins.filter.mathstuff import intersect
from jinja2 import Environment

@pytest.fixture
def environment():
    return Environment()

def test_intersect_hashable(environment):
    a = {1, 2, 3}
    b = {2, 3, 4}
    result = intersect(environment, a, b)
    assert set(result) == {2, 3}

def test_intersect_non_hashable(environment):
    a = [1, 2, 3, 4]
    b = [3, 4, 5, 6]
    result = intersect(environment, a, b)
    assert result == [3, 4]

def test_intersect_mixed_types(environment):
    a = [1, 2, 3, 4]
    b = {3, 4, 5, 6}
    result = intersect(environment, a, b)
    assert result == [3, 4]
