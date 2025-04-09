# file: typesystem/schemas.py:51-89
# asked: {"lines": [51, 52, 57, 59, 61, 62, 63, 64, 67, 68, 69, 70, 71, 74, 75, 76, 80, 81, 84, 85, 87, 88, 89], "branches": [[61, 62], [61, 67], [62, 61], [62, 63], [67, 68], [67, 74], [69, 67], [69, 70], [70, 69], [70, 71], [74, 75], [74, 80], [75, 76], [75, 80], [87, 88], [87, 89]]}
# gained: {"lines": [51, 52, 57, 59, 61, 62, 63, 64, 67, 68, 69, 70, 71, 74, 75, 76, 80, 81, 84, 85, 87, 88, 89], "branches": [[61, 62], [61, 67], [62, 61], [62, 63], [67, 68], [67, 74], [69, 67], [69, 70], [70, 71], [74, 75], [74, 80], [75, 76], [75, 80], [87, 88], [87, 89]]}

import pytest
from typesystem.fields import Field, String, Integer
from typesystem.schemas import SchemaMetaclass

class TestSchemaMetaclass:
    def test_schema_metaclass_new(self):
        class TestField(Field):
            _creation_counter = 0

        class BaseSchema(metaclass=SchemaMetaclass):
            base_field = TestField()

        class ChildSchema(BaseSchema):
            child_field = TestField()

        definitions = {}
        attrs = {
            'child_field': TestField()
        }
        name = 'ChildSchema'
        bases = (BaseSchema,)
        
        new_type = SchemaMetaclass.__new__(SchemaMetaclass, name, bases, attrs, definitions)
        
        assert 'base_field' in new_type.fields
        assert 'child_field' in new_type.fields
        assert definitions['ChildSchema'] == new_type

    def test_schema_metaclass_with_definitions(self, mocker):
        class TestField(Field):
            _creation_counter = 0

        class BaseSchema(metaclass=SchemaMetaclass):
            base_field = TestField()

        class ChildSchema(BaseSchema):
            child_field = TestField()

        definitions = {}
        attrs = {
            'child_field': TestField()
        }
        name = 'ChildSchema'
        bases = (BaseSchema,)
        
        mock_set_definitions = mocker.patch('typesystem.schemas.set_definitions')
        
        new_type = SchemaMetaclass.__new__(SchemaMetaclass, name, bases, attrs, definitions)
        
        mock_set_definitions.assert_called()
        assert 'base_field' in new_type.fields
        assert 'child_field' in new_type.fields
        assert definitions['ChildSchema'] == new_type
