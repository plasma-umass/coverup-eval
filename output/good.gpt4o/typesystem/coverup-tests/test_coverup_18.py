# file typesystem/schemas.py:32-48
# lines [32, 37, 38, 39, 40, 41, 42, 43, 45, 46, 47, 48]
# branches ['37->38', '37->39', '39->40', '39->46', '40->exit', '40->41', '41->42', '41->45', '42->exit', '42->43', '46->exit', '46->47', '47->exit', '47->48']

import pytest
from typesystem.schemas import set_definitions, Field, Reference, Array, Object, SchemaDefinitions

def test_set_definitions():
    definitions = SchemaDefinitions()

    # Test with Reference field
    ref_field = Reference(to="SomeType", definitions=None)
    set_definitions(ref_field, definitions)
    assert ref_field.definitions is definitions

    # Test with Array field containing a single item
    array_field_single = Array(items=Reference(to="SomeType", definitions=None))
    set_definitions(array_field_single, definitions)
    assert array_field_single.items.definitions is definitions

    # Test with Array field containing multiple items
    array_field_multiple = Array(items=[Reference(to="SomeType", definitions=None), Reference(to="SomeType", definitions=None)])
    set_definitions(array_field_multiple, definitions)
    assert all(item.definitions is definitions for item in array_field_multiple.items)

    # Test with Object field
    object_field = Object(properties={"child": Reference(to="SomeType", definitions=None)})
    set_definitions(object_field, definitions)
    assert object_field.properties["child"].definitions is definitions

    # Test with nested structures
    nested_field = Object(properties={
        "array": Array(items=[
            Reference(to="SomeType", definitions=None),
            Object(properties={"nested_child": Reference(to="SomeType", definitions=None)})
        ])
    })
    set_definitions(nested_field, definitions)
    assert nested_field.properties["array"].items[0].definitions is definitions
    assert nested_field.properties["array"].items[1].properties["nested_child"].definitions is definitions
