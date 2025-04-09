# file: lib/ansible/plugins/filter/mathstuff.py:119-125
# asked: {"lines": [121, 122, 124, 125], "branches": [[121, 122], [121, 124]]}
# gained: {"lines": [121, 122, 124, 125], "branches": [[121, 122], [121, 124]]}

import pytest
from ansible.plugins.filter.mathstuff import union
from ansible.module_utils.common._collections_compat import Hashable
from jinja2 import Environment

def test_union_with_hashable(monkeypatch):
    class MockHashable:
        def __init__(self, items):
            self.items = items

        def __iter__(self):
            return iter(self.items)

        def __hash__(self):
            return hash(tuple(self.items))

        def __eq__(self, other):
            return self.items == other.items

    a = MockHashable([1, 2, 3])
    b = MockHashable([3, 4, 5])
    env = Environment()

    result = union(env, a, b)
    assert result == {1, 2, 3, 4, 5}

def test_union_with_non_hashable(monkeypatch):
    def mock_unique(environment, a, case_sensitive):
        return list(set(a))

    monkeypatch.setattr('ansible.plugins.filter.mathstuff.unique', mock_unique)

    a = [1, 2, 3]
    b = [3, 4, 5]
    env = Environment()

    result = union(env, a, b)
    assert result == [1, 2, 3, 4, 5]
