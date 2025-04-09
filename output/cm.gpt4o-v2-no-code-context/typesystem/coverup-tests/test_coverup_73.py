# file: typesystem/json_schema.py:199-331
# asked: {"lines": [250, 252, 253, 260, 264, 265, 282, 291, 292, 302, 306, 307, 312], "branches": [[249, 250], [251, 252], [259, 260], [261, 264], [281, 282], [290, 291], [301, 302], [303, 306], [311, 312]]}
# gained: {"lines": [250, 252, 253, 260, 264, 265, 282, 291, 292, 302, 306, 307, 312], "branches": [[249, 250], [251, 252], [259, 260], [261, 264], [281, 282], [290, 291], [301, 302], [303, 306], [311, 312]]}

import pytest
from typesystem.json_schema import from_json_schema_type, SchemaDefinitions, Field, Float, Integer, String, Boolean, Array, Object, NO_DEFAULT

def test_from_json_schema_type_array_items_none():
    data = {"type": "array"}
    type_string = "array"
    allow_null = False
    definitions = SchemaDefinitions()
    
    result = from_json_schema_type(data, type_string, allow_null, definitions)
    
    assert isinstance(result, Array)
    assert result.items is None

def test_from_json_schema_type_array_items_list(monkeypatch):
    data = {"type": "array", "items": [{"type": "string"}, {"type": "integer"}]}
    type_string = "array"
    allow_null = False
    definitions = SchemaDefinitions()
    
    def mock_from_json_schema(item, definitions):
        if item["type"] == "string":
            return String()
        elif item["type"] == "integer":
            return Integer()
    
    monkeypatch.setattr('typesystem.json_schema.from_json_schema', mock_from_json_schema)
    
    result = from_json_schema_type(data, type_string, allow_null, definitions)
    
    assert isinstance(result, Array)
    assert isinstance(result.items[0], String)
    assert isinstance(result.items[1], Integer)

def test_from_json_schema_type_array_additional_items_none():
    data = {"type": "array", "items": {"type": "string"}}
    type_string = "array"
    allow_null = False
    definitions = SchemaDefinitions()
    
    result = from_json_schema_type(data, type_string, allow_null, definitions)
    
    assert isinstance(result, Array)
    assert result.additional_items is True

def test_from_json_schema_type_array_additional_items_field(monkeypatch):
    data = {"type": "array", "items": {"type": "string"}, "additionalItems": {"type": "integer"}}
    type_string = "array"
    allow_null = False
    definitions = SchemaDefinitions()
    
    def mock_from_json_schema(item, definitions):
        if item["type"] == "string":
            return String()
        elif item["type"] == "integer":
            return Integer()
    
    monkeypatch.setattr('typesystem.json_schema.from_json_schema', mock_from_json_schema)
    
    result = from_json_schema_type(data, type_string, allow_null, definitions)
    
    assert isinstance(result, Array)
    assert isinstance(result.additional_items, Integer)

def test_from_json_schema_type_object_properties_none():
    data = {"type": "object"}
    type_string = "object"
    allow_null = False
    definitions = SchemaDefinitions()
    
    result = from_json_schema_type(data, type_string, allow_null, definitions)
    
    assert isinstance(result, Object)
    assert result.properties == {}

def test_from_json_schema_type_object_pattern_properties_none():
    data = {"type": "object", "properties": {"name": {"type": "string"}}}
    type_string = "object"
    allow_null = False
    definitions = SchemaDefinitions()
    
    result = from_json_schema_type(data, type_string, allow_null, definitions)
    
    assert isinstance(result, Object)
    assert result.pattern_properties == {}

def test_from_json_schema_type_object_additional_properties_none():
    data = {"type": "object", "properties": {"name": {"type": "string"}}}
    type_string = "object"
    allow_null = False
    definitions = SchemaDefinitions()
    
    result = from_json_schema_type(data, type_string, allow_null, definitions)
    
    assert isinstance(result, Object)
    assert result.additional_properties is None

def test_from_json_schema_type_object_additional_properties_field(monkeypatch):
    data = {"type": "object", "properties": {"name": {"type": "string"}}, "additionalProperties": {"type": "integer"}}
    type_string = "object"
    allow_null = False
    definitions = SchemaDefinitions()
    
    def mock_from_json_schema(item, definitions):
        if item["type"] == "string":
            return String()
        elif item["type"] == "integer":
            return Integer()
    
    monkeypatch.setattr('typesystem.json_schema.from_json_schema', mock_from_json_schema)
    
    result = from_json_schema_type(data, type_string, allow_null, definitions)
    
    assert isinstance(result, Object)
    assert isinstance(result.additional_properties, Integer)

def test_from_json_schema_type_object_property_names_none():
    data = {"type": "object", "properties": {"name": {"type": "string"}}}
    type_string = "object"
    allow_null = False
    definitions = SchemaDefinitions()
    
    result = from_json_schema_type(data, type_string, allow_null, definitions)
    
    assert isinstance(result, Object)
    assert result.property_names is None
