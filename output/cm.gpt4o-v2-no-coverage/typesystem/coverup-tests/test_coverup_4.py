# file: typesystem/fields.py:661-674
# asked: {"lines": [661, 662, 663, 665, 666, 667, 668, 671, 672, 674], "branches": [[662, 663], [662, 665], [665, 666], [665, 671], [671, 672], [671, 674]]}
# gained: {"lines": [661, 662, 663, 665, 666, 667, 668, 671, 672, 674], "branches": [[662, 663], [662, 665], [665, 666], [665, 671], [671, 672], [671, 674]]}

import pytest
from typesystem.fields import Array, Field

class MockField(Field):
    def serialize(self, obj):
        return f"serialized-{obj}"

def test_serialize_none():
    array_field = Array(items=None)
    assert array_field.serialize(None) is None

def test_serialize_with_list_of_serializers():
    array_field = Array(items=[MockField(), MockField()])
    result = array_field.serialize(["item1", "item2"])
    assert result == ["serialized-item1", "serialized-item2"]

def test_serialize_with_single_serializer():
    array_field = Array(items=MockField())
    result = array_field.serialize(["item1", "item2"])
    assert result == ["serialized-item1", "serialized-item2"]

def test_serialize_with_no_items():
    array_field = Array(items=None)
    result = array_field.serialize(["item1", "item2"])
    assert result == ["item1", "item2"]
