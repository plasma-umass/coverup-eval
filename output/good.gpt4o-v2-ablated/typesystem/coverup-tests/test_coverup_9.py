# file: typesystem/fields.py:562-600
# asked: {"lines": [562, 564, 565, 566, 567, 568, 569, 572, 574, 576, 577, 578, 579, 581, 582, 583, 584, 586, 587, 588, 589, 590, 592, 593, 594, 596, 597, 598, 599, 600], "branches": [[586, 587], [586, 592], [587, 588], [587, 589], [589, 590], [589, 592], [592, 593], [592, 596]]}
# gained: {"lines": [562, 564, 565, 566, 567, 568, 569, 572, 574, 576, 577, 578, 579, 581, 582, 583, 584, 586, 587, 588, 589, 590, 592, 593, 594, 596, 597, 598, 599, 600], "branches": [[586, 587], [586, 592], [587, 588], [587, 589], [589, 590], [589, 592], [592, 593], [592, 596]]}

import pytest
from typesystem.fields import Field, Array

class MockField(Field):
    pass

@pytest.fixture
def mock_field():
    return MockField()

def test_array_init_with_defaults():
    array = Array()
    assert array.items is None
    assert array.additional_items is False
    assert array.min_items is None
    assert array.max_items is None
    assert array.unique_items is False

def test_array_init_with_single_item(mock_field):
    array = Array(items=mock_field)
    assert array.items == mock_field
    assert array.min_items is None
    assert array.max_items is None

def test_array_init_with_multiple_items(mock_field):
    items = [mock_field, mock_field]
    array = Array(items=items)
    assert array.items == items
    assert array.min_items == len(items)
    assert array.max_items == len(items)

def test_array_init_with_additional_items(mock_field):
    array = Array(items=[mock_field], additional_items=True)
    assert array.additional_items is True
    assert array.min_items == 1
    assert array.max_items is None

def test_array_init_with_min_max_items(mock_field):
    array = Array(items=[mock_field], min_items=1, max_items=2)
    assert array.min_items == 1
    assert array.max_items == 2

def test_array_init_with_exact_items(mock_field):
    array = Array(items=[mock_field], exact_items=1)
    assert array.min_items == 1
    assert array.max_items == 1

def test_array_init_with_unique_items(mock_field):
    array = Array(items=[mock_field], unique_items=True)
    assert array.unique_items is True

def test_array_init_invalid_items():
    with pytest.raises(AssertionError):
        Array(items="invalid")

def test_array_init_invalid_additional_items():
    with pytest.raises(AssertionError):
        Array(additional_items="invalid")

def test_array_init_invalid_min_items():
    with pytest.raises(AssertionError):
        Array(min_items="invalid")

def test_array_init_invalid_max_items():
    with pytest.raises(AssertionError):
        Array(max_items="invalid")

def test_array_init_invalid_unique_items():
    with pytest.raises(AssertionError):
        Array(unique_items="invalid")
