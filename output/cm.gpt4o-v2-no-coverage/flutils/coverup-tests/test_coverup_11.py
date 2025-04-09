# file: flutils/objutils.py:146-203
# asked: {"lines": [146, 201, 202, 203], "branches": [[201, 202], [201, 203]]}
# gained: {"lines": [146, 201, 202, 203], "branches": [[201, 202], [201, 203]]}

import pytest
from collections import UserList, deque
from collections.abc import Iterator, KeysView, ValuesView
from flutils.objutils import is_list_like

def test_is_list_like():
    # Test cases that should return True
    assert is_list_like([1, 2, 3]) == True
    assert is_list_like(reversed([1, 2, 4])) == True
    assert is_list_like(sorted('hello')) == True
    assert is_list_like(UserList([1, 2, 3])) == True
    assert is_list_like(deque([1, 2, 3])) == True
    assert is_list_like((1, 2, 3)) == True
    assert is_list_like({1, 2, 3}) == True
    assert is_list_like(frozenset([1, 2, 3])) == True
    assert is_list_like({}.keys()) == True
    assert is_list_like({}.values()) == True

    # Test cases that should return False
    assert is_list_like(None) == False
    assert is_list_like(True) == False
    assert is_list_like(b"bytes") == False
    assert is_list_like("string") == False
    assert is_list_like(123) == False
    assert is_list_like(123.456) == False
    assert is_list_like({}) == False

