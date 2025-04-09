# file: typesystem/schemas.py:32-48
# asked: {"lines": [45], "branches": [[41, 45], [46, 0]]}
# gained: {"lines": [], "branches": [[46, 0]]}

import pytest
from typesystem.fields import Array, Field, Object
from typesystem.schemas import set_definitions, Reference, SchemaDefinitions

def test_set_definitions_with_reference():
    reference = Reference(to="SomeSchema")
    definitions = SchemaDefinitions()
    set_definitions(reference, definitions)
    assert reference.definitions is definitions

def test_set_definitions_with_array_of_references():
    reference1 = Reference(to="SomeSchema1")
    reference2 = Reference(to="SomeSchema2")
    array = Array(items=[reference1, reference2])
    definitions = SchemaDefinitions()
    set_definitions(array, definitions)
    assert reference1.definitions is definitions
    assert reference2.definitions is definitions

def test_set_definitions_with_array_of_non_references():
    field1 = Field()
    field2 = Field()
    array = Array(items=[field1, field2])
    definitions = SchemaDefinitions()
    set_definitions(array, definitions)
    # Field objects do not have a 'definitions' attribute, so we check that no error is raised
    assert not hasattr(field1, 'definitions')
    assert not hasattr(field2, 'definitions')

def test_set_definitions_with_object():
    reference = Reference(to="SomeSchema")
    properties = {"ref": reference, "field": Field()}
    obj = Object(properties=properties)
    definitions = SchemaDefinitions()
    set_definitions(obj, definitions)
    assert reference.definitions is definitions
    assert not hasattr(properties["field"], 'definitions')

def test_set_definitions_with_nested_objects():
    reference = Reference(to="SomeSchema")
    nested_obj = Object(properties={"ref": reference})
    obj = Object(properties={"nested": nested_obj})
    definitions = SchemaDefinitions()
    set_definitions(obj, definitions)
    assert reference.definitions is definitions
    assert nested_obj.properties["ref"].definitions is definitions
