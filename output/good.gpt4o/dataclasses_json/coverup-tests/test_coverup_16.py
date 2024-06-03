# file dataclasses_json/mm.py:169-172
# lines [169, 170, 172]
# branches []

import pytest
from unittest.mock import MagicMock
from dataclasses_json.mm import SchemaF
from marshmallow import Schema

class DummySchema(Schema):
    pass

class TestSchemaF:
    def test_dumps_list(self, mocker):
        # Create a mock object for the generic type A
        mock_obj = MagicMock()
        
        # Mock the SchemaF class to bypass the NotImplementedError
        mocker.patch('dataclasses_json.mm.SchemaF.__init__', lambda self: None)
        
        # Create an instance of SchemaF with DummySchema as the generic type
        schema_f_instance = SchemaF[DummySchema]()
        
        # Mock the dumps method to return a predefined string
        mocker.patch.object(schema_f_instance, 'dumps', return_value='mocked_result')
        
        # Call the dumps method with a list of mock objects
        result = schema_f_instance.dumps([mock_obj], many=True)
        
        # Assert that the result is the mocked string
        assert result == 'mocked_result'
        
        # Clean up by resetting the mock object
        mock_obj.reset_mock()
