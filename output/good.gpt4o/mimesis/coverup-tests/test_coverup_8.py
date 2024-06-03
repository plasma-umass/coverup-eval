# file mimesis/schema.py:118-140
# lines [118, 119, 121, 126, 127, 129, 131, 140]
# branches ['126->127', '126->129']

import pytest
from mimesis.schema import Schema
from mimesis.exceptions import UndefinedSchema

def test_schema_initialization_with_callable():
    def dummy_schema():
        return {"key": "value"}
    
    schema_instance = Schema(dummy_schema)
    assert schema_instance.schema == dummy_schema

def test_schema_initialization_with_non_callable():
    with pytest.raises(UndefinedSchema):
        Schema("not a callable")

def test_schema_create_method():
    def dummy_schema():
        return {"key": "value"}
    
    schema_instance = Schema(dummy_schema)
    result = schema_instance.create(iterations=3)
    assert result == [{"key": "value"}, {"key": "value"}, {"key": "value"}]

def test_schema_create_method_default_iterations():
    def dummy_schema():
        return {"key": "value"}
    
    schema_instance = Schema(dummy_schema)
    result = schema_instance.create()
    assert result == [{"key": "value"}]
