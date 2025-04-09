# file: typesystem/fields.py:562-600
# asked: {"lines": [], "branches": [[587, 589], [589, 592]]}
# gained: {"lines": [], "branches": [[589, 592]]}

import pytest
from typesystem.fields import Field, Array

class DummyField(Field):
    pass

def test_array_min_items_none_with_list_items():
    items = [DummyField(), DummyField()]
    array = Array(items=items, min_items=None)
    assert array.min_items == len(items)

def test_array_max_items_none_with_list_items_and_additional_items_false():
    items = [DummyField(), DummyField()]
    array = Array(items=items, max_items=None, additional_items=False)
    assert array.max_items == len(items)

def test_array_min_and_max_items_none_with_list_items_and_additional_items_true():
    items = [DummyField(), DummyField()]
    array = Array(items=items, min_items=None, max_items=None, additional_items=True)
    assert array.min_items == len(items)
    assert array.max_items is None

def test_array_exact_items():
    exact_items = 3
    array = Array(exact_items=exact_items)
    assert array.min_items == exact_items
    assert array.max_items == exact_items
