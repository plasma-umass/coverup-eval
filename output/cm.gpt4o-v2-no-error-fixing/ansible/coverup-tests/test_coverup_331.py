# file: lib/ansible/plugins/filter/mathstuff.py:119-125
# asked: {"lines": [119, 120, 121, 122, 124, 125], "branches": [[121, 122], [121, 124]]}
# gained: {"lines": [119, 120, 121, 122, 124, 125], "branches": [[121, 122], [121, 124]]}

import pytest
from unittest.mock import MagicMock
from ansible.plugins.filter.mathstuff import union
from ansible.module_utils.common._collections_compat import Hashable

def test_union_with_hashable(monkeypatch):
    environment = MagicMock()
    a = frozenset([1, 2, 3])
    b = frozenset([3, 4, 5])
    
    result = union(environment, a, b)
    
    assert result == set([1, 2, 3, 4, 5])

def test_union_with_non_hashable(monkeypatch):
    def mock_unique(env, seq, case_sensitive):
        return list(set(seq))
    
    monkeypatch.setattr('ansible.plugins.filter.mathstuff.unique', mock_unique)
    
    environment = MagicMock()
    a = [1, 2, 3]
    b = [3, 4, 5]
    
    result = union(environment, a, b)
    
    assert result == [1, 2, 3, 4, 5]
