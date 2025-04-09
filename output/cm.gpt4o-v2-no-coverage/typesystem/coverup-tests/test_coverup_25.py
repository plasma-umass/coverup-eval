# file: typesystem/schemas.py:32-48
# asked: {"lines": [32, 37, 38, 39, 40, 41, 42, 43, 45, 46, 47, 48], "branches": [[37, 38], [37, 39], [39, 40], [39, 46], [40, 0], [40, 41], [41, 42], [41, 45], [42, 0], [42, 43], [46, 0], [46, 47], [47, 0], [47, 48]]}
# gained: {"lines": [32, 37, 38, 39, 40, 41, 42, 43, 46, 47, 48], "branches": [[37, 38], [37, 39], [39, 40], [39, 46], [40, 0], [40, 41], [41, 42], [42, 0], [42, 43], [46, 47], [47, 0], [47, 48]]}

import pytest
from typesystem.fields import Array, Field, Object
from typesystem.schemas import set_definitions, Reference, SchemaDefinitions

def test_set_definitions_with_reference():
    field = Reference(to="SomeSchema")
    definitions = SchemaDefinitions()
    set_definitions(field, definitions)
    assert field.definitions is definitions

def test_set_definitions_with_array_of_references():
    field = Array(items=[Reference(to="SomeSchema"), Reference(to="AnotherSchema")])
    definitions = SchemaDefinitions()
    set_definitions(field, definitions)
    for item in field.items:
        assert item.definitions is definitions

def test_set_definitions_with_array_of_objects():
    field = Array(items=[Object(properties={"child": Reference(to="SomeSchema")})])
    definitions = SchemaDefinitions()
    set_definitions(field, definitions)
    for item in field.items:
        for child in item.properties.values():
            assert child.definitions is definitions

def test_set_definitions_with_object():
    field = Object(properties={"child": Reference(to="SomeSchema")})
    definitions = SchemaDefinitions()
    set_definitions(field, definitions)
    for child in field.properties.values():
        assert child.definitions is definitions

def test_set_definitions_with_empty_array():
    field = Array(items=[])
    definitions = SchemaDefinitions()
    set_definitions(field, definitions)
    assert field.items == []

def test_set_definitions_with_none_items():
    field = Array(items=None)
    definitions = SchemaDefinitions()
    set_definitions(field, definitions)
    assert field.items is None
