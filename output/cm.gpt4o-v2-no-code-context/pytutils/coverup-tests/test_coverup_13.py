# file: pytutils/path.py:4-6
# asked: {"lines": [4, 5, 6], "branches": [[5, 0], [5, 6]]}
# gained: {"lines": [4, 5, 6], "branches": [[5, 0], [5, 6]]}

import os
import pytest

from pytutils.path import join_each

def test_join_each(monkeypatch):
    parent = "/parent"
    iterable = ["child1", "child2", "child3"]
    
    expected = [os.path.join(parent, p) for p in iterable]
    
    result = list(join_each(parent, iterable))
    
    assert result == expected
