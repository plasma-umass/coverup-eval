# file: pytutils/path.py:4-6
# asked: {"lines": [4, 5, 6], "branches": [[5, 0], [5, 6]]}
# gained: {"lines": [4, 5, 6], "branches": [[5, 0], [5, 6]]}

import os
import pytest

from pytutils.path import join_each

def test_join_each():
    parent = "/home/user"
    iterable = ["docs", "images", "videos"]
    expected = [os.path.join(parent, "docs"), os.path.join(parent, "images"), os.path.join(parent, "videos")]
    
    result = list(join_each(parent, iterable))
    
    assert result == expected

def test_join_each_empty_iterable():
    parent = "/home/user"
    iterable = []
    expected = []
    
    result = list(join_each(parent, iterable))
    
    assert result == expected

def test_join_each_with_absolute_path():
    parent = "/home/user"
    iterable = ["/etc/passwd", "images", "/var/log"]
    expected = [os.path.join(parent, "/etc/passwd"), os.path.join(parent, "images"), os.path.join(parent, "/var/log")]
    
    result = list(join_each(parent, iterable))
    
    assert result == expected
