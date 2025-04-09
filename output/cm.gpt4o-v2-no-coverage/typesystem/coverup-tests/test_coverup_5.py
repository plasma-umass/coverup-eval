# file: typesystem/schemas.py:51-89
# asked: {"lines": [51, 52, 57, 59, 61, 62, 63, 64, 67, 68, 69, 70, 71, 74, 75, 76, 80, 81, 84, 85, 87, 88, 89], "branches": [[61, 62], [61, 67], [62, 61], [62, 63], [67, 68], [67, 74], [69, 67], [69, 70], [70, 69], [70, 71], [74, 75], [74, 80], [75, 76], [75, 80], [87, 88], [87, 89]]}
# gained: {"lines": [51, 52, 57, 59, 61, 62, 63, 64, 67, 68, 69, 70, 71, 74, 75, 76, 80, 81, 84, 85, 87, 88, 89], "branches": [[61, 62], [61, 67], [62, 61], [62, 63], [67, 68], [67, 74], [69, 67], [69, 70], [70, 71], [74, 75], [74, 80], [75, 76], [75, 80], [87, 88], [87, 89]]}

import pytest
from typesystem.fields import Field
from typesystem.schemas import SchemaMetaclass

class MockField(Field):
    _creation_counter = 0

    def __init__(self):
        super().__init__()
        MockField._creation_counter += 1
        self._creation_counter = MockField._creation_counter

def set_definitions(field, definitions):
    field.definitions = definitions

class TestSchemaMetaclass:
    def test_schema_metaclass_new(self, mocker):
        mocker.patch('typesystem.schemas.set_definitions', side_effect=set_definitions)
        
        class BaseSchema(metaclass=SchemaMetaclass):
            base_field = MockField()

        class ChildSchema(BaseSchema, metaclass=SchemaMetaclass):
            child_field = MockField()

        assert 'base_field' in ChildSchema.fields
        assert 'child_field' in ChildSchema.fields
        assert ChildSchema.fields['base_field']._creation_counter < ChildSchema.fields['child_field']._creation_counter

        definitions = {}
        class SchemaWithDefinitions(metaclass=SchemaMetaclass, definitions=definitions):
            field_with_def = MockField()

        assert 'field_with_def' in SchemaWithDefinitions.fields
        assert definitions['SchemaWithDefinitions'] is SchemaWithDefinitions
        assert SchemaWithDefinitions.fields['field_with_def'].definitions is definitions
