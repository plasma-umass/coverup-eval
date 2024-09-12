# file: typesystem/json_schema.py:334-337
# asked: {"lines": [334, 335, 336, 337], "branches": []}
# gained: {"lines": [334, 335, 336, 337], "branches": []}

import pytest
from typesystem.json_schema import ref_from_json_schema
from typesystem.schemas import SchemaDefinitions, Reference

def test_ref_from_json_schema():
    data = {"$ref": "#/definitions/example"}
    definitions = SchemaDefinitions()
    
    result = ref_from_json_schema(data, definitions)
    
    assert isinstance(result, Reference)
    assert result.to == "#/definitions/example"
    assert result.definitions == definitions

def test_ref_from_json_schema_invalid_ref():
    data = {"$ref": "http://example.com/schema"}
    definitions = SchemaDefinitions()
    
    with pytest.raises(AssertionError, match="Unsupported \\$ref style in document."):
        ref_from_json_schema(data, definitions)
