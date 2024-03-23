# file typesystem/schemas.py:51-89
# lines [51, 52, 57, 59, 61, 62, 63, 64, 67, 68, 69, 70, 71, 74, 75, 76, 80, 81, 84, 85, 87, 88, 89]
# branches ['61->62', '61->67', '62->61', '62->63', '67->68', '67->74', '69->67', '69->70', '70->69', '70->71', '74->75', '74->80', '75->76', '75->80', '87->88', '87->89']

import pytest
from typesystem.fields import Field
from typesystem.schemas import SchemaMetaclass, SchemaDefinitions

class TestField(Field):
    _creation_counter = 0

    def __init__(self):
        super().__init__()
        self.__class__._creation_counter += 1

def test_schema_metaclass_definitions():
    definitions = SchemaDefinitions()

    class BaseSchema(metaclass=SchemaMetaclass, definitions=definitions):
        base_field = TestField()

    class ChildSchema(BaseSchema, metaclass=SchemaMetaclass, definitions=definitions):
        child_field = TestField()

    assert 'BaseSchema' in definitions
    assert 'ChildSchema' in definitions
    assert isinstance(ChildSchema.fields['base_field'], TestField)
    assert isinstance(ChildSchema.fields['child_field'], TestField)
    assert ChildSchema.fields['base_field']._creation_counter < ChildSchema.fields['child_field']._creation_counter
