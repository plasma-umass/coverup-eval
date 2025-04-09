# file: lib/ansible/plugins/filter/mathstuff.py:91-97
# asked: {"lines": [94], "branches": [[93, 94]]}
# gained: {"lines": [94], "branches": [[93, 94]]}

import pytest
from ansible.plugins.filter.mathstuff import intersect
from jinja2 import Environment

@pytest.fixture
def environment():
    return Environment()

def test_intersect_with_hashable(environment):
    a = frozenset([1, 2, 3])
    b = frozenset([2, 3, 4])
    result = intersect(environment, a, b)
    assert result == frozenset([2, 3])

def test_intersect_with_non_hashable(environment):
    a = [1, 2, 3]
    b = [2, 3, 4]
    result = intersect(environment, a, b)
    assert result == [2, 3]
