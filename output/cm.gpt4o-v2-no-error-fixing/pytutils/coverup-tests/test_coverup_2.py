# file: pytutils/path.py:4-6
# asked: {"lines": [4, 5, 6], "branches": [[5, 0], [5, 6]]}
# gained: {"lines": [4, 5, 6], "branches": [[5, 0], [5, 6]]}

import os
import pytest
from pytutils.path import join_each

def test_join_each():
    parent = "/home/user"
    iterable = ["file1.txt", "file2.txt", "file3.txt"]
    expected = [os.path.join(parent, p) for p in iterable]
    
    result = list(join_each(parent, iterable))
    
    assert result == expected
