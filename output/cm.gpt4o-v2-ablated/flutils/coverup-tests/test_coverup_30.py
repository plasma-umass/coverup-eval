# file: flutils/objutils.py:146-203
# asked: {"lines": [146, 201, 202, 203], "branches": [[201, 202], [201, 203]]}
# gained: {"lines": [146, 201, 202, 203], "branches": [[201, 202], [201, 203]]}

import pytest
from collections import UserList, deque, ChainMap, Counter, OrderedDict, UserDict, UserString, defaultdict
from decimal import Decimal
from flutils.objutils import is_list_like

class MockClass:
    pass

def is_subclass_of_any(obj, *classes):
    return isinstance(obj, classes)

_LIST_LIKE = (UserList, list, tuple, deque, set, frozenset)

@pytest.mark.parametrize("obj, expected", [
    ([1, 2, 3], True),
    (reversed([1, 2, 4]), True),
    ('hello', False),
    (sorted('hello'), True),
    (UserList([1, 2, 3]), True),
    (deque([1, 2, 3]), True),
    (set([1, 2, 3]), True),
    (frozenset([1, 2, 3]), True),
    (tuple([1, 2, 3]), True),
    (None, False),
    (True, False),
    (b'bytes', False),
    (ChainMap(), False),
    (Counter(), False),
    (OrderedDict(), False),
    (UserDict(), False),
    (UserString('string'), False),
    (defaultdict(list), False),
    (Decimal(10), False),
    ({'key': 'value'}, False),
    (3.14, False),
    (42, False),
    (MockClass(), False)
])
def test_is_list_like(obj, expected, monkeypatch):
    monkeypatch.setattr('flutils.objutils.is_subclass_of_any', is_subclass_of_any)
    assert is_list_like(obj) == expected
