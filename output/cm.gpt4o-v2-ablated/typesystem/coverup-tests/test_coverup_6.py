# file: typesystem/fields.py:661-674
# asked: {"lines": [661, 662, 663, 665, 666, 667, 668, 671, 672, 674], "branches": [[662, 663], [662, 665], [665, 666], [665, 671], [671, 672], [671, 674]]}
# gained: {"lines": [661, 662, 663, 665, 666, 667, 668, 671, 672, 674], "branches": [[662, 663], [662, 665], [665, 666], [665, 671], [671, 672], [671, 674]]}

import pytest
from typesystem.fields import Array
from typesystem import Field

class MockField(Field):
    def serialize(self, value):
        return f"serialized-{value}"

@pytest.fixture
def mock_field():
    return MockField()

def test_array_serialize_none():
    array_field = Array()
    assert array_field.serialize(None) is None

def test_array_serialize_with_items_list(mock_field):
    array_field = Array(items=[mock_field, mock_field])
    result = array_field.serialize(["value1", "value2"])
    assert result == ["serialized-value1", "serialized-value2"]

def test_array_serialize_with_items_none():
    array_field = Array(items=None)
    result = array_field.serialize(["value1", "value2"])
    assert result == ["value1", "value2"]

def test_array_serialize_with_single_item(mock_field):
    array_field = Array(items=mock_field)
    result = array_field.serialize(["value1", "value2"])
    assert result == ["serialized-value1", "serialized-value2"]
