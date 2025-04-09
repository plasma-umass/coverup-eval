# file: typesystem/fields.py:661-674
# asked: {"lines": [661, 662, 663, 665, 666, 667, 668, 671, 672, 674], "branches": [[662, 663], [662, 665], [665, 666], [665, 671], [671, 672], [671, 674]]}
# gained: {"lines": [661, 662, 663, 665, 666, 667, 668, 671, 672, 674], "branches": [[662, 663], [662, 665], [665, 666], [665, 671], [671, 672], [671, 674]]}

import pytest
from typesystem.fields import Array, Field

class MockField(Field):
    def serialize(self, obj):
        return f"serialized-{obj}"

def test_array_serialize_none():
    array_field = Array()
    assert array_field.serialize(None) is None

def test_array_serialize_with_list_items():
    item1 = MockField()
    item2 = MockField()
    array_field = Array(items=[item1, item2])
    result = array_field.serialize(["value1", "value2"])
    assert result == ["serialized-value1", "serialized-value2"]

def test_array_serialize_with_none_items():
    array_field = Array(items=None)
    result = array_field.serialize(["value1", "value2"])
    assert result == ["value1", "value2"]

def test_array_serialize_with_single_item():
    item = MockField()
    array_field = Array(items=item)
    result = array_field.serialize(["value1", "value2"])
    assert result == ["serialized-value1", "serialized-value2"]
