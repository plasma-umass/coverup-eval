# file: typesystem/schemas.py:32-48
# asked: {"lines": [32, 37, 38, 39, 40, 41, 42, 43, 45, 46, 47, 48], "branches": [[37, 38], [37, 39], [39, 40], [39, 46], [40, 0], [40, 41], [41, 42], [41, 45], [42, 0], [42, 43], [46, 0], [46, 47], [47, 0], [47, 48]]}
# gained: {"lines": [32, 37, 38, 39, 40, 41, 42, 43, 46, 47, 48], "branches": [[37, 38], [37, 39], [39, 40], [39, 46], [40, 41], [41, 42], [42, 0], [42, 43], [46, 0], [46, 47], [47, 0], [47, 48]]}

import pytest
from typesystem.fields import Array, Field, Object
from typesystem.schemas import set_definitions, Reference, SchemaDefinitions

def test_set_definitions_with_reference():
    definitions = SchemaDefinitions()
    reference = Reference(to="SomeSchema")
    set_definitions(reference, definitions)
    assert reference.definitions is definitions

def test_set_definitions_with_array_of_references():
    definitions = SchemaDefinitions()
    reference1 = Reference(to="SomeSchema1")
    reference2 = Reference(to="SomeSchema2")
    array_field = Array(items=[reference1, reference2])
    set_definitions(array_field, definitions)
    assert reference1.definitions is definitions
    assert reference2.definitions is definitions

def test_set_definitions_with_array_of_non_references():
    definitions = SchemaDefinitions()
    non_reference = Field()
    array_field = Array(items=[non_reference])
    set_definitions(array_field, definitions)
    # No assertion needed for non_reference as it does not have definitions attribute

def test_set_definitions_with_object():
    definitions = SchemaDefinitions()
    reference = Reference(to="SomeSchema")
    object_field = Object(properties={"ref": reference})
    set_definitions(object_field, definitions)
    assert reference.definitions is definitions

def test_set_definitions_with_nested_objects_and_arrays():
    definitions = SchemaDefinitions()
    reference1 = Reference(to="SomeSchema1")
    reference2 = Reference(to="SomeSchema2")
    array_field = Array(items=[reference1])
    object_field = Object(properties={"array": array_field, "ref": reference2})
    set_definitions(object_field, definitions)
    assert reference1.definitions is definitions
    assert reference2.definitions is definitions
