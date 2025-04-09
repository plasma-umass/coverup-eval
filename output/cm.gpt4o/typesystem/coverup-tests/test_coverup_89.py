# file typesystem/schemas.py:32-48
# lines []
# branches ['40->exit']

import pytest
from typesystem.schemas import set_definitions, Field, Reference, Array, Object, SchemaDefinitions

def test_set_definitions_array_items_none():
    # Create a mock for SchemaDefinitions
    definitions = SchemaDefinitions()

    # Create an Array field with items set to None
    array_field = Array(items=None)

    # Call set_definitions and ensure it does not raise an exception
    set_definitions(array_field, definitions)

    # Assert that the items attribute is still None
    assert array_field.items is None

def test_set_definitions_array_items_list():
    # Create a mock for SchemaDefinitions
    definitions = SchemaDefinitions()

    # Create a list of Reference fields
    ref1 = Reference(to="SomeSchema", definitions=None)
    ref2 = Reference(to="SomeSchema", definitions=None)

    # Create an Array field with items as a list of Reference fields
    array_field = Array(items=[ref1, ref2])

    # Call set_definitions
    set_definitions(array_field, definitions)

    # Assert that the definitions attribute of each Reference field is set
    assert ref1.definitions is definitions
    assert ref2.definitions is definitions

def test_set_definitions_array_items_single():
    # Create a mock for SchemaDefinitions
    definitions = SchemaDefinitions()

    # Create a single Reference field
    ref = Reference(to="SomeSchema", definitions=None)

    # Create an Array field with items as a single Reference field
    array_field = Array(items=ref)

    # Call set_definitions
    set_definitions(array_field, definitions)

    # Assert that the definitions attribute of the Reference field is set
    assert ref.definitions is definitions
