# file lib/ansible/plugins/filter/mathstuff.py:100-106
# lines [103]
# branches ['102->103']

import pytest
from ansible.plugins.filter.mathstuff import difference
from jinja2 import Environment

@pytest.fixture
def environment():
    return Environment()

def test_difference_with_hashable(environment):
    a = frozenset([1, 2, 3])
    b = frozenset([2, 3, 4])
    result = difference(environment, a, b)
    assert result == {1}

def test_difference_with_non_hashable(environment):
    a = [1, 2, 3]
    b = [2, 3, 4]
    result = difference(environment, a, b)
    assert result == [1]
