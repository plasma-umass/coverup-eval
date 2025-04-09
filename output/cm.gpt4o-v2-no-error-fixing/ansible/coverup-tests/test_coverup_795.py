# file: lib/ansible/plugins/filter/mathstuff.py:91-97
# asked: {"lines": [93, 94, 96, 97], "branches": [[93, 94], [93, 96]]}
# gained: {"lines": [93, 94, 96, 97], "branches": [[93, 94], [93, 96]]}

import pytest
from ansible.plugins.filter.mathstuff import intersect
from jinja2 import Environment

def test_intersect_with_hashable(monkeypatch):
    env = Environment()
    a = frozenset([1, 2, 3])
    b = frozenset([2, 3, 4])
    result = intersect(env, a, b)
    assert result == {2, 3}

def test_intersect_with_non_hashable(monkeypatch):
    env = Environment()
    
    def mock_unique(environment, a, case_sensitive):
        return list(set(a))
    
    monkeypatch.setattr('ansible.plugins.filter.mathstuff.unique', mock_unique)
    
    a = [1, 2, 3, 4]
    b = [2, 3, 5]
    result = intersect(env, a, b)
    assert result == [2, 3]
