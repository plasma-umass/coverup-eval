# file lib/ansible/plugins/filter/mathstuff.py:100-106
# lines [100, 101, 102, 103, 105, 106]
# branches ['102->103', '102->105']

import pytest
from ansible.plugins.filter.mathstuff import difference
from jinja2 import Environment

@pytest.fixture
def environment():
    return Environment()

def test_difference_hashable(environment):
    a = {1, 2, 3}
    b = {2, 3, 4}
    result = difference(environment, a, b)
    assert set(result) == {1}

def test_difference_non_hashable(environment):
    a = [1, 2, 3]
    b = [2, 3, 4]
    result = difference(environment, a, b)
    assert result == [1]

def test_difference_mixed_types(environment):
    a = [1, 2, 3, 'a']
    b = [2, 3, 4, 'b']
    result = difference(environment, a, b)
    assert result == [1, 'a']
