# file typesystem/schemas.py:160-164
# lines [160, 161, 164]
# branches []

import pytest
from typesystem.schemas import Schema, SchemaMetaclass

class TestSchema:
    def test_is_sparse(self, mocker):
        # Mocking the fields attribute to simulate different scenarios
        mock_fields = mocker.patch.object(Schema, 'fields', create=True)
        
        # Case 1: No fields
        mock_fields.keys.return_value = []
        schema_instance = Schema()
        assert not schema_instance.is_sparse, "Expected is_sparse to be False when there are no fields"

        # Case 2: All fields have attributes
        mock_fields.keys.return_value = ['field1', 'field2']
        setattr(schema_instance, 'field1', 'value1')
        setattr(schema_instance, 'field2', 'value2')
        assert not schema_instance.is_sparse, "Expected is_sparse to be False when all fields have attributes"

        # Case 3: Some fields do not have attributes
        delattr(schema_instance, 'field2')
        assert schema_instance.is_sparse, "Expected is_sparse to be True when some fields do not have attributes"
