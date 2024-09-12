# file: lib/ansible/plugins/filter/mathstuff.py:100-106
# asked: {"lines": [100, 101, 102, 103, 105, 106], "branches": [[102, 103], [102, 105]]}
# gained: {"lines": [100, 101, 102, 103, 105, 106], "branches": [[102, 103], [102, 105]]}

import pytest
from jinja2 import Environment
from ansible.plugins.filter.mathstuff import difference
from ansible.module_utils.common._collections_compat import Hashable

def test_difference_hashable(monkeypatch):
    class MockHashable:
        def __init__(self, value):
            self.value = value

        def __hash__(self):
            return hash(self.value)

        def __eq__(self, other):
            return self.value == other.value

        def __iter__(self):
            return iter([self.value])

    a = MockHashable(1)
    b = MockHashable(2)
    env = Environment()

    monkeypatch.setattr(Hashable, "__instancecheck__", lambda self, instance: isinstance(instance, MockHashable))

    result = difference(env, a, b)
    assert result == set([1])

def test_difference_non_hashable(monkeypatch):
    def mock_unique(environment, a, case_sensitive):
        return a

    monkeypatch.setattr('ansible.plugins.filter.mathstuff.unique', mock_unique)

    a = [1, 2, 3]
    b = [2]
    env = Environment()

    result = difference(env, a, b)
    assert result == [1, 3]
