# file: typesystem/schemas.py:32-48
# asked: {"lines": [45], "branches": [[40, 0], [41, 45]]}
# gained: {"lines": [45], "branches": [[40, 0], [41, 45]]}

import pytest
from typesystem.fields import Array, Field, Object
from typesystem.schemas import set_definitions

class MockSchemaDefinitions:
    pass

def test_set_definitions_with_array_items_none():
    array_field = Array(items=None)
    definitions = MockSchemaDefinitions()
    set_definitions(array_field, definitions)
    assert array_field.items is None

def test_set_definitions_with_array_items_field():
    item_field = Field()
    array_field = Array(items=item_field)
    definitions = MockSchemaDefinitions()
    set_definitions(array_field, definitions)
    assert array_field.items is item_field

def test_set_definitions_with_array_items_list():
    item_field1 = Field()
    item_field2 = Field()
    array_field = Array(items=[item_field1, item_field2])
    definitions = MockSchemaDefinitions()
    set_definitions(array_field, definitions)
    assert array_field.items == [item_field1, item_field2]

def test_set_definitions_with_object():
    property_field = Field()
    object_field = Object(properties={"prop": property_field})
    definitions = MockSchemaDefinitions()
    set_definitions(object_field, definitions)
    assert object_field.properties["prop"] is property_field
