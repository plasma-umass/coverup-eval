# file: typesystem/unique.py:24-26
# asked: {"lines": [24, 25, 26], "branches": []}
# gained: {"lines": [24, 25, 26], "branches": []}

import pytest
from typesystem.unique import Uniqueness

@pytest.fixture
def uniqueness():
    class TestUniqueness(Uniqueness):
        TRUE = 'true'
        FALSE = 'false'
        def __init__(self):
            self._set = set()
    return TestUniqueness()

def test_add_with_primitive(uniqueness):
    uniqueness.add(1)
    assert 1 in uniqueness._set

def test_add_with_list(uniqueness):
    uniqueness.add([1, 2, 3])
    assert ('list', (1, 2, 3)) in uniqueness._set

def test_add_with_dict(uniqueness):
    uniqueness.add({'key': 'value'})
    assert ('dict', (('key', 'value'),)) in uniqueness._set

def test_add_with_true(uniqueness):
    uniqueness.add(True)
    assert uniqueness.TRUE in uniqueness._set

def test_add_with_false(uniqueness):
    uniqueness.add(False)
    assert uniqueness.FALSE in uniqueness._set
