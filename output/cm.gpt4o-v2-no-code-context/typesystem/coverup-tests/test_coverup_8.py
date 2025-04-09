# file: typesystem/schemas.py:51-89
# asked: {"lines": [51, 52, 57, 59, 61, 62, 63, 64, 67, 68, 69, 70, 71, 74, 75, 76, 80, 81, 84, 85, 87, 88, 89], "branches": [[61, 62], [61, 67], [62, 61], [62, 63], [67, 68], [67, 74], [69, 67], [69, 70], [70, 69], [70, 71], [74, 75], [74, 80], [75, 76], [75, 80], [87, 88], [87, 89]]}
# gained: {"lines": [51, 52, 57, 59, 61, 62, 63, 64, 67, 68, 69, 70, 71, 74, 75, 76, 80, 81, 84, 85, 87, 88, 89], "branches": [[61, 62], [61, 67], [62, 61], [62, 63], [67, 68], [67, 74], [69, 67], [69, 70], [70, 71], [74, 75], [74, 80], [75, 76], [75, 80], [87, 88], [87, 89]]}

import pytest
from typesystem.schemas import SchemaMetaclass, Field, SchemaDefinitions, set_definitions

class TestSchemaMetaclass:
    def test_schema_metaclass_new_with_fields(self):
        class TestField(Field):
            _creation_counter = 0

        class TestSchema(metaclass=SchemaMetaclass):
            field1 = TestField()
            field2 = TestField()

        assert hasattr(TestSchema, 'fields')
        assert 'field1' in TestSchema.fields
        assert 'field2' in TestSchema.fields

    def test_schema_metaclass_new_with_base_class(self):
        class TestField(Field):
            _creation_counter = 0

        class BaseSchema(metaclass=SchemaMetaclass):
            base_field = TestField()

        class TestSchema(BaseSchema):
            field1 = TestField()

        assert hasattr(TestSchema, 'fields')
        assert 'base_field' in TestSchema.fields
        assert 'field1' in TestSchema.fields

    def test_schema_metaclass_new_with_definitions(self, mocker):
        class TestField(Field):
            _creation_counter = 0

        definitions = SchemaDefinitions()
        mock_set_definitions = mocker.patch('typesystem.schemas.set_definitions')

        class TestSchema(metaclass=SchemaMetaclass, definitions=definitions):
            field1 = TestField()

        assert hasattr(TestSchema, 'fields')
        assert 'field1' in TestSchema.fields
        mock_set_definitions.assert_called_once_with(TestSchema.fields['field1'], definitions)
        assert definitions['TestSchema'] == TestSchema

    def test_schema_metaclass_new_field_order(self):
        class TestField(Field):
            _creation_counter = 0

        class TestSchema(metaclass=SchemaMetaclass):
            field2 = TestField()
            field1 = TestField()

        fields = list(TestSchema.fields.keys())
        assert fields == ['field2', 'field1']
