# file typesystem/fields.py:562-600
# lines []
# branches ['587->589', '589->592']

import pytest
from typesystem.fields import Field, Array

def test_array_field_min_max_items():
    class DummyField(Field):
        pass

    # Test case to cover the branch 587->589
    items = [DummyField(), DummyField()]
    array_field = Array(items=items)
    assert array_field.min_items == len(items)
    assert array_field.max_items == len(items)

    # Test case to cover the branch 589->592
    array_field = Array(items=items, additional_items=True)
    assert array_field.min_items == len(items)
    assert array_field.max_items is None

    # Test case to cover the branch 592
    exact_items = 3
    array_field = Array(items=items, exact_items=exact_items)
    assert array_field.min_items == exact_items
    assert array_field.max_items == exact_items
