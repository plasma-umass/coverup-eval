# file: f058/__init__.py:1-8
# asked: {"lines": [1, 3, 4, 5, 6, 7, 8], "branches": [[4, 5], [4, 8], [5, 4], [5, 6], [6, 5], [6, 7]]}
# gained: {"lines": [1, 3, 4, 5, 6, 7, 8], "branches": [[4, 5], [4, 8], [5, 4], [5, 6], [6, 5], [6, 7]]}

import pytest
from f058 import common

def test_common_with_common_elements():
    l1 = [1, 2, 3, 4]
    l2 = [3, 4, 5, 6]
    result = common(l1, l2)
    assert result == [3, 4]

def test_common_with_no_common_elements():
    l1 = [1, 2]
    l2 = [3, 4]
    result = common(l1, l2)
    assert result == []

def test_common_with_empty_lists():
    l1 = []
    l2 = []
    result = common(l1, l2)
    assert result == []

def test_common_with_one_empty_list():
    l1 = [1, 2, 3]
    l2 = []
    result = common(l1, l2)
    assert result == []

    l1 = []
    l2 = [1, 2, 3]
    result = common(l1, l2)
    assert result == []
