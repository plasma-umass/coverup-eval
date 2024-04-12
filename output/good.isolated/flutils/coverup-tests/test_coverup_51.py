# file flutils/objutils.py:146-203
# lines [146, 201, 202, 203]
# branches ['201->202', '201->203']

import pytest
from collections import UserList, deque, ChainMap, Counter, OrderedDict, UserDict, UserString, defaultdict
from collections.abc import Iterator, KeysView, ValuesView
from decimal import Decimal
from flutils.objutils import is_list_like

_LIST_LIKE = (
    UserList,
    Iterator,
    KeysView,
    ValuesView,
    deque,
    frozenset,
    list,
    set,
    tuple,
)

def test_is_list_like():
    # Test with list-like objects
    assert is_list_like(UserList([1, 2, 3])) is True
    assert is_list_like(iter([1, 2, 3])) is True
    assert is_list_like({}.keys()) is True
    assert is_list_like({}.values()) is True
    assert is_list_like(deque([1, 2, 3])) is True
    assert is_list_like(frozenset([1, 2, 3])) is True
    assert is_list_like([1, 2, 3]) is True
    assert is_list_like({1, 2, 3}) is True
    assert is_list_like((1, 2, 3)) is True

    # Test with non-list-like objects
    assert is_list_like(None) is False
    assert is_list_like(True) is False
    assert is_list_like(b'bytes') is False
    assert is_list_like(ChainMap()) is False
    assert is_list_like(Counter()) is False
    assert is_list_like(OrderedDict()) is False
    assert is_list_like(UserDict()) is False
    assert is_list_like(UserString('string')) is False
    assert is_list_like(defaultdict(int)) is False
    assert is_list_like(Decimal('10.5')) is False
    assert is_list_like({}) is False
    assert is_list_like(1.0) is False
    assert is_list_like(1) is False
    assert is_list_like('string') is False
