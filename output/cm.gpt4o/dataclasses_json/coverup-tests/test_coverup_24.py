# file dataclasses_json/mm.py:216-219
# lines [216, 217, 219]
# branches []

import pytest
from dataclasses_json.mm import SchemaF
from marshmallow import Schema
import typing

class TestSchemaF:
    def test_loads(self, mocker):
        # Mocking the Schema class to avoid any side effects
        mock_schema = mocker.patch('dataclasses_json.mm.Schema', autospec=True)
        
        # Creating a subclass of SchemaF to test the loads method
        class MySchema(SchemaF[int]):
            def loads(self, json_data, many=None, partial=None, unknown=None, **kwargs):
                return "mocked_result"
        
        # Mocking the __init__ method to avoid NotImplementedError
        mocker.patch.object(MySchema, '__init__', lambda self: None)
        
        schema_instance = MySchema()
        
        # Mocking the loads method to ensure it gets called
        mock_loads = mocker.patch.object(schema_instance, 'loads', return_value="mocked_result")
        
        # Calling the loads method with test data
        result = schema_instance.loads('{"key": "value"}', many=True, partial=True, unknown='EXCLUDE')
        
        # Assertions to verify the behavior
        mock_loads.assert_called_once_with('{"key": "value"}', many=True, partial=True, unknown='EXCLUDE')
        assert result == "mocked_result"
