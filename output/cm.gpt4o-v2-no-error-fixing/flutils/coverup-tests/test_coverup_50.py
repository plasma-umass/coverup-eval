# file: flutils/objutils.py:146-203
# asked: {"lines": [201, 202, 203], "branches": [[201, 202], [201, 203]]}
# gained: {"lines": [201, 202, 203], "branches": [[201, 202], [201, 203]]}

import pytest
from collections import UserList, deque
from collections.abc import Iterator, KeysView, ValuesView
from flutils.objutils import is_list_like

def test_is_list_like_with_list():
    assert is_list_like([1, 2, 3]) == True

def test_is_list_like_with_iterator():
    assert is_list_like(iter([1, 2, 3])) == True

def test_is_list_like_with_keysview():
    assert is_list_like({1: 'a', 2: 'b'}.keys()) == True

def test_is_list_like_with_valuesview():
    assert is_list_like({1: 'a', 2: 'b'}.values()) == True

def test_is_list_like_with_deque():
    assert is_list_like(deque([1, 2, 3])) == True

def test_is_list_like_with_frozenset():
    assert is_list_like(frozenset([1, 2, 3])) == True

def test_is_list_like_with_set():
    assert is_list_like({1, 2, 3}) == True

def test_is_list_like_with_tuple():
    assert is_list_like((1, 2, 3)) == True

def test_is_list_like_with_userlist():
    assert is_list_like(UserList([1, 2, 3])) == True

def test_is_list_like_with_none():
    assert is_list_like(None) == False

def test_is_list_like_with_bool():
    assert is_list_like(True) == False

def test_is_list_like_with_bytes():
    assert is_list_like(b'hello') == False

def test_is_list_like_with_chainmap():
    from collections import ChainMap
    assert is_list_like(ChainMap({1: 'a'}, {2: 'b'})) == False

def test_is_list_like_with_counter():
    from collections import Counter
    assert is_list_like(Counter([1, 2, 3])) == False

def test_is_list_like_with_ordereddict():
    from collections import OrderedDict
    assert is_list_like(OrderedDict({1: 'a', 2: 'b'})) == False

def test_is_list_like_with_userdict():
    from collections import UserDict
    assert is_list_like(UserDict({1: 'a', 2: 'b'})) == False

def test_is_list_like_with_userstring():
    from collections import UserString
    assert is_list_like(UserString('hello')) == False

def test_is_list_like_with_defaultdict():
    from collections import defaultdict
    assert is_list_like(defaultdict(list)) == False

def test_is_list_like_with_decimal():
    from decimal import Decimal
    assert is_list_like(Decimal(10.5)) == False

def test_is_list_like_with_dict():
    assert is_list_like({1: 'a', 2: 'b'}) == False

def test_is_list_like_with_float():
    assert is_list_like(10.5) == False

def test_is_list_like_with_int():
    assert is_list_like(10) == False

def test_is_list_like_with_str():
    assert is_list_like('hello') == False
