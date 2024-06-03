# file flutils/objutils.py:146-203
# lines [146, 201, 202, 203]
# branches ['201->202', '201->203']

import pytest
from collections import UserList, deque, ChainMap, Counter, OrderedDict, UserDict, UserString, defaultdict
from collections.abc import KeysView, ValuesView, Iterable
from decimal import Decimal
from flutils.objutils import is_list_like

class CustomListLike:
    def __iter__(self):
        return iter([1, 2, 3])

class CustomNotListLike:
    pass

def is_subclass_of_any(obj, *classes):
    return isinstance(obj, classes) or any(isinstance(obj, cls) for cls in classes)

_LIST_LIKE = (UserList, deque, KeysView, ValuesView, frozenset, list, set, tuple, Iterable)

@pytest.mark.parametrize("obj, expected", [
    ([1, 2, 3], True),
    (reversed([1, 2, 4]), True),
    ('hello', False),
    (sorted('hello'), True),
    (UserList([1, 2, 3]), True),
    (deque([1, 2, 3]), True),
    (KeysView({'a': 1, 'b': 2}), True),
    (ValuesView({'a': 1, 'b': 2}), True),
    (frozenset([1, 2, 3]), True),
    (set([1, 2, 3]), True),
    (tuple([1, 2, 3]), True),
    (None, False),
    (True, False),
    (b'bytes', False),
    (ChainMap({'a': 1}), False),
    (Counter([1, 2, 3]), False),
    (OrderedDict({'a': 1}), False),
    (UserDict({'a': 1}), False),
    (UserString('hello'), False),
    (defaultdict(list), False),
    (Decimal('10.5'), False),
    ({'a': 1, 'b': 2}, False),
    (3.14, False),
    (42, False),
    (CustomListLike(), False),  # Corrected to False as CustomListLike is not in _LIST_LIKE
    (CustomNotListLike(), False),
])
def test_is_list_like(obj, expected):
    assert is_list_like(obj) == expected
