# file typesystem/schemas.py:51-89
# lines [51, 52, 57, 59, 61, 62, 63, 64, 67, 68, 69, 70, 71, 74, 75, 76, 80, 81, 84, 85, 87, 88, 89]
# branches ['61->62', '61->67', '62->61', '62->63', '67->68', '67->74', '69->67', '69->70', '70->69', '70->71', '74->75', '74->80', '75->76', '75->80', '87->88', '87->89']

import pytest
from unittest.mock import MagicMock
from typesystem.schemas import SchemaMetaclass, Field, SchemaDefinitions

class TestSchemaMetaclass:
    def test_schema_metaclass(self):
        # Mocking Field and SchemaDefinitions
        mock_field = MagicMock(spec=Field)
        mock_field._creation_counter = 1
        mock_definitions = MagicMock(spec=SchemaDefinitions)

        # Creating a test class using the SchemaMetaclass
        class BaseSchema(metaclass=SchemaMetaclass):
            base_field = mock_field

        class TestSchema(BaseSchema, metaclass=SchemaMetaclass, definitions=mock_definitions):
            test_field = mock_field

        # Assertions to verify the fields and definitions
        assert 'base_field' in TestSchema.fields
        assert 'test_field' in TestSchema.fields
        assert TestSchema.fields['base_field'] == mock_field
        assert TestSchema.fields['test_field'] == mock_field
        mock_definitions.__setitem__.assert_called_with('TestSchema', TestSchema)
