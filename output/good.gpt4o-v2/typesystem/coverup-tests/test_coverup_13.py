# file: typesystem/fields.py:562-600
# asked: {"lines": [562, 564, 565, 566, 567, 568, 569, 572, 574, 576, 577, 578, 579, 581, 582, 583, 584, 586, 587, 588, 589, 590, 592, 593, 594, 596, 597, 598, 599, 600], "branches": [[586, 587], [586, 592], [587, 588], [587, 589], [589, 590], [589, 592], [592, 593], [592, 596]]}
# gained: {"lines": [562, 564, 565, 566, 567, 568, 569, 572, 574, 576, 577, 578, 579, 581, 582, 583, 584, 586, 587, 588, 589, 590, 592, 593, 594, 596, 597, 598, 599, 600], "branches": [[586, 587], [586, 592], [587, 588], [589, 590], [592, 593], [592, 596]]}

import pytest
from typesystem.fields import Array, Field

def test_array_init_with_none_items():
    array = Array()
    assert array.items is None
    assert array.additional_items is False
    assert array.min_items is None
    assert array.max_items is None
    assert array.unique_items is False

def test_array_init_with_field_item():
    item = Field()
    array = Array(items=item)
    assert array.items == item
    assert array.additional_items is False
    assert array.min_items is None
    assert array.max_items is None
    assert array.unique_items is False

def test_array_init_with_list_of_fields():
    item1 = Field()
    item2 = Field()
    array = Array(items=[item1, item2])
    assert array.items == [item1, item2]
    assert array.additional_items is False
    assert array.min_items == 2
    assert array.max_items == 2
    assert array.unique_items is False

def test_array_init_with_additional_items_field():
    additional_item = Field()
    array = Array(additional_items=additional_item)
    assert array.additional_items == additional_item

def test_array_init_with_min_items():
    array = Array(min_items=5)
    assert array.min_items == 5

def test_array_init_with_max_items():
    array = Array(max_items=10)
    assert array.max_items == 10

def test_array_init_with_exact_items():
    array = Array(exact_items=3)
    assert array.min_items == 3
    assert array.max_items == 3

def test_array_init_with_unique_items():
    array = Array(unique_items=True)
    assert array.unique_items is True

def test_array_init_with_invalid_items():
    with pytest.raises(AssertionError):
        Array(items="invalid")

def test_array_init_with_invalid_additional_items():
    with pytest.raises(AssertionError):
        Array(additional_items="invalid")

def test_array_init_with_invalid_min_items():
    with pytest.raises(AssertionError):
        Array(min_items="invalid")

def test_array_init_with_invalid_max_items():
    with pytest.raises(AssertionError):
        Array(max_items="invalid")

def test_array_init_with_invalid_unique_items():
    with pytest.raises(AssertionError):
        Array(unique_items="invalid")
