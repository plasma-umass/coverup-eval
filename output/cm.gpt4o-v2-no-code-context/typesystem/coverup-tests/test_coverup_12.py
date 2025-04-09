# file: typesystem/fields.py:562-600
# asked: {"lines": [562, 564, 565, 566, 567, 568, 569, 572, 574, 576, 577, 578, 579, 581, 582, 583, 584, 586, 587, 588, 589, 590, 592, 593, 594, 596, 597, 598, 599, 600], "branches": [[586, 587], [586, 592], [587, 588], [587, 589], [589, 590], [589, 592], [592, 593], [592, 596]]}
# gained: {"lines": [562, 564, 565, 566, 567, 568, 569, 572, 574, 576, 577, 578, 579, 581, 582, 583, 584, 586, 587, 588, 589, 590, 592, 593, 594, 596, 597, 598, 599, 600], "branches": [[586, 587], [586, 592], [587, 588], [589, 590], [592, 593], [592, 596]]}

import pytest
from typesystem.fields import Array, Field

class DummyField(Field):
    pass

def test_array_init_with_no_items():
    array = Array()
    assert array.items is None
    assert array.additional_items is False
    assert array.min_items is None
    assert array.max_items is None
    assert array.unique_items is False

def test_array_init_with_single_item():
    item = DummyField()
    array = Array(items=item)
    assert array.items == item
    assert array.additional_items is False
    assert array.min_items is None
    assert array.max_items is None
    assert array.unique_items is False

def test_array_init_with_multiple_items():
    items = [DummyField(), DummyField()]
    array = Array(items=items)
    assert array.items == items
    assert array.additional_items is False
    assert array.min_items == len(items)
    assert array.max_items == len(items)
    assert array.unique_items is False

def test_array_init_with_additional_items():
    item = DummyField()
    array = Array(items=item, additional_items=True)
    assert array.items == item
    assert array.additional_items is True
    assert array.min_items is None
    assert array.max_items is None
    assert array.unique_items is False

def test_array_init_with_min_max_items():
    item = DummyField()
    array = Array(items=item, min_items=1, max_items=5)
    assert array.items == item
    assert array.additional_items is False
    assert array.min_items == 1
    assert array.max_items == 5
    assert array.unique_items is False

def test_array_init_with_exact_items():
    items = [DummyField(), DummyField()]
    array = Array(items=items, exact_items=2)
    assert array.items == items
    assert array.additional_items is False
    assert array.min_items == 2
    assert array.max_items == 2
    assert array.unique_items is False

def test_array_init_with_unique_items():
    item = DummyField()
    array = Array(items=item, unique_items=True)
    assert array.items == item
    assert array.additional_items is False
    assert array.min_items is None
    assert array.max_items is None
    assert array.unique_items is True

def test_array_init_with_invalid_items():
    with pytest.raises(AssertionError):
        Array(items="invalid")

def test_array_init_with_invalid_additional_items():
    with pytest.raises(AssertionError):
        Array(items=DummyField(), additional_items="invalid")

def test_array_init_with_invalid_min_items():
    with pytest.raises(AssertionError):
        Array(items=DummyField(), min_items="invalid")

def test_array_init_with_invalid_max_items():
    with pytest.raises(AssertionError):
        Array(items=DummyField(), max_items="invalid")

def test_array_init_with_invalid_unique_items():
    with pytest.raises(AssertionError):
        Array(items=DummyField(), unique_items="invalid")
