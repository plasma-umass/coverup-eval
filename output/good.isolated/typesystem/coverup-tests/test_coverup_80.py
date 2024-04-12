# file typesystem/schemas.py:51-89
# lines []
# branches ['70->69']

import pytest
from typesystem.fields import Field
from typesystem.schemas import SchemaMetaclass, SchemaDefinitions

class BaseSchema(metaclass=SchemaMetaclass):
    base_field = Field()

class TestSchema(metaclass=SchemaMetaclass):
    pass

def test_schema_metaclass_with_inherited_field():
    class InheritedSchema(BaseSchema, metaclass=SchemaMetaclass):
        pass

    assert 'base_field' in InheritedSchema.fields
    assert isinstance(InheritedSchema.fields['base_field'], Field)

def test_schema_metaclass_with_overridden_field():
    class OverriddenSchema(BaseSchema, metaclass=SchemaMetaclass):
        base_field = Field()

    assert 'base_field' in OverriddenSchema.fields
    assert isinstance(OverriddenSchema.fields['base_field'], Field)
    assert OverriddenSchema.fields['base_field'] is not BaseSchema.fields['base_field']

def test_schema_metaclass_with_definitions():
    definitions = SchemaDefinitions()
    class SchemaWithDefinitions(metaclass=SchemaMetaclass, definitions=definitions):
        field_with_definition = Field()

    assert 'SchemaWithDefinitions' in definitions
    assert definitions['SchemaWithDefinitions'] is SchemaWithDefinitions
