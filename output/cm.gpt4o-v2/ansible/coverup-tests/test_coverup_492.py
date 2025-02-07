# file: lib/ansible/plugins/filter/mathstuff.py:91-97
# asked: {"lines": [91, 92, 93, 94, 96, 97], "branches": [[93, 94], [93, 96]]}
# gained: {"lines": [91, 92, 93, 94, 96, 97], "branches": [[93, 94], [93, 96]]}

import pytest
from jinja2 import Environment
from ansible.plugins.filter.mathstuff import intersect
from ansible.module_utils.common._collections_compat import Hashable

def test_intersect_hashable(monkeypatch):
    env = Environment()

    class MockHashable:
        def __init__(self, items):
            self.items = items

        def __iter__(self):
            return iter(self.items)

        def __hash__(self):
            return hash(tuple(self.items))

    a = MockHashable([1, 2, 3])
    b = MockHashable([2, 3, 4])

    result = intersect(env, a, b)
    assert result == {2, 3}

def test_intersect_non_hashable(monkeypatch):
    env = Environment()

    def mock_unique(environment, a, case_sensitive):
        return list(set(a))

    monkeypatch.setattr('ansible.plugins.filter.mathstuff.unique', mock_unique)

    a = [1, 2, 3, 4]
    b = [3, 4, 5, 6]

    result = intersect(env, a, b)
    assert result == [3, 4]
