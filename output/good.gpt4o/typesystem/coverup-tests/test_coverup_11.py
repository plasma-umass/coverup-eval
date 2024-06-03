# file typesystem/schemas.py:184-187
# lines [184, 185, 186, 187]
# branches ['185->exit', '185->186', '186->185', '186->187']

import pytest
from typesystem.schemas import Schema, SchemaMetaclass

class TestSchema:
    def test_schema_iter(self, mocker):
        # Mock the fields attribute and an instance attribute
        mock_fields = ['field1', 'field2']
        mock_instance = mocker.MagicMock(spec=Schema)
        mock_instance.fields = mock_fields
        mock_instance.field1 = 'value1'
        mock_instance.field2 = 'value2'
        
        # Patch the Schema class to use the mock instance
        mocker.patch.object(Schema, '__init__', lambda self: None)
        schema_instance = Schema()
        schema_instance.fields = mock_fields
        schema_instance.field1 = 'value1'
        schema_instance.field2 = 'value2'
        
        # Collect the keys from the iterator
        keys = list(schema_instance.__iter__())
        
        # Assertions to verify the correct keys are yielded
        assert keys == ['field1', 'field2']
