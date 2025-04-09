# file typesystem/json_schema.py:334-337
# lines [334, 335, 336, 337]
# branches []

import pytest
from typesystem.fields import Field
from typesystem.schemas import SchemaDefinitions
from typesystem.json_schema import ref_from_json_schema

def test_ref_from_json_schema():
    definitions = SchemaDefinitions()
    data = {"$ref": "#/definitions/MyModel"}

    # Test that the function returns a Reference instance
    reference = ref_from_json_schema(data, definitions)
    assert isinstance(reference, Field)

    # Test that the reference has the correct 'to' attribute
    assert reference.to == data["$ref"]

    # Test that the reference has the correct 'definitions' attribute
    assert reference.definitions is definitions

def test_ref_from_json_schema_with_invalid_ref():
    definitions = SchemaDefinitions()
    data = {"$ref": "http://example.com/definitions/MyModel"}

    # Test that the function raises an AssertionError for unsupported $ref style
    with pytest.raises(AssertionError) as excinfo:
        ref_from_json_schema(data, definitions)
    assert "Unsupported $ref style in document." in str(excinfo.value)
