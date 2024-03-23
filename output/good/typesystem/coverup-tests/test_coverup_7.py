# file typesystem/fields.py:562-600
# lines [562, 564, 565, 566, 567, 568, 569, 572, 574, 576, 577, 578, 579, 581, 582, 583, 584, 586, 587, 588, 589, 590, 592, 593, 594, 596, 597, 598, 599, 600]
# branches ['586->587', '586->592', '587->588', '587->589', '589->590', '589->592', '592->593', '592->596']

import pytest
from typesystem.fields import Array, Field

class MockField(Field):
    pass

def test_array_field_initialization():
    # Test with items as a list of Fields
    items_list = [MockField(), MockField()]
    array_field = Array(items=items_list)
    assert array_field.items == items_list
    assert array_field.min_items == len(items_list)
    assert array_field.max_items == len(items_list)

    # Test with items as a single Field
    single_item = MockField()
    array_field = Array(items=single_item)
    assert array_field.items == single_item

    # Test with additional_items as a Field
    additional_item = MockField()
    array_field = Array(additional_items=additional_item)
    assert array_field.additional_items == additional_item

    # Test with min_items and max_items
    array_field = Array(min_items=1, max_items=5)
    assert array_field.min_items == 1
    assert array_field.max_items == 5

    # Test with exact_items
    array_field = Array(exact_items=3)
    assert array_field.min_items == 3
    assert array_field.max_items == 3

    # Test with unique_items
    array_field = Array(unique_items=True)
    assert array_field.unique_items is True

    # Test with additional_items as bool
    array_field = Array(additional_items=True)
    assert array_field.additional_items is True

    # Test with no items and additional_items as False
    array_field = Array()
    assert array_field.items is None
    assert array_field.additional_items is False
    assert array_field.min_items is None
    assert array_field.max_items is None

    # Test with items as a tuple of Fields
    items_tuple = (MockField(), MockField())
    array_field = Array(items=items_tuple)
    assert array_field.items == list(items_tuple)
    assert array_field.min_items == len(items_tuple)
    assert array_field.max_items == len(items_tuple)

@pytest.fixture(autouse=True)
def clean():
    # Fixture to clean up after each test case
    yield

# The following line is just for local testing and should not be included in the final script
# pytest.main()
