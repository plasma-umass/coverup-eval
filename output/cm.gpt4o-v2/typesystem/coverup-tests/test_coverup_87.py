# file: typesystem/schemas.py:51-89
# asked: {"lines": [70, 71, 75, 76, 88], "branches": [[69, 70], [70, 69], [70, 71], [74, 75], [75, 76], [75, 80], [87, 88]]}
# gained: {"lines": [70, 71, 75, 76, 88], "branches": [[69, 70], [70, 71], [74, 75], [75, 76], [75, 80], [87, 88]]}

import pytest
from typesystem.fields import Field, String, Integer
from typesystem.schemas import SchemaMetaclass, set_definitions

class TestSchemaMetaclass:
    def test_inherited_fields(self):
        class BaseSchema(metaclass=SchemaMetaclass):
            base_field = String()

        class ChildSchema(BaseSchema):
            child_field = Integer()

        assert 'base_field' in ChildSchema.fields
        assert 'child_field' in ChildSchema.fields

    def test_set_definitions_called(self, mocker):
        mock_set_definitions = mocker.patch('typesystem.schemas.set_definitions')

        definitions = {}

        class TestSchema(metaclass=SchemaMetaclass):
            test_field = String()

        SchemaMetaclass.__new__(SchemaMetaclass, 'TestSchema', (object,), {'test_field': String()}, definitions)

        mock_set_definitions.assert_called_once()

    def test_definitions_updated(self):
        definitions = {}

        class TestSchema(metaclass=SchemaMetaclass):
            test_field = String()

        TestSchema = SchemaMetaclass.__new__(SchemaMetaclass, 'TestSchema', (object,), {'test_field': String()}, definitions)

        assert 'TestSchema' in definitions
        assert definitions['TestSchema'] is TestSchema
