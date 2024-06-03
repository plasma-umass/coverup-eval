# file typesystem/json_schema.py:334-337
# lines [334, 335, 336, 337]
# branches []

import pytest
from typesystem.json_schema import ref_from_json_schema, SchemaDefinitions, Reference

def test_ref_from_json_schema():
    definitions = SchemaDefinitions()
    data = {"$ref": "#/definitions/example"}
    
    result = ref_from_json_schema(data, definitions)
    
    assert isinstance(result, Reference)
    assert result.to == "#/definitions/example"
    assert result.definitions is definitions

def test_ref_from_json_schema_invalid_ref():
    definitions = SchemaDefinitions()
    data = {"$ref": "http://example.com/schema"}
    
    with pytest.raises(AssertionError, match="Unsupported \\$ref style in document."):
        ref_from_json_schema(data, definitions)
