# file: typesystem/json_schema.py:334-337
# asked: {"lines": [335, 336, 337], "branches": []}
# gained: {"lines": [335, 336, 337], "branches": []}

import pytest
from typesystem.json_schema import ref_from_json_schema, SchemaDefinitions, Reference

def test_ref_from_json_schema_valid_ref():
    data = {"$ref": "#/definitions/Example"}
    definitions = SchemaDefinitions()
    result = ref_from_json_schema(data, definitions)
    assert isinstance(result, Reference)
    assert result.to == "#/definitions/Example"
    assert result.definitions == definitions

def test_ref_from_json_schema_invalid_ref():
    data = {"$ref": "http://example.com/schema"}
    definitions = SchemaDefinitions()
    with pytest.raises(AssertionError, match=r"Unsupported \$ref style in document\."):
        ref_from_json_schema(data, definitions)
