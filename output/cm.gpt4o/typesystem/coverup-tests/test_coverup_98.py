# file typesystem/schemas.py:51-89
# lines []
# branches ['70->69']

import pytest
from unittest.mock import MagicMock
from typesystem.schemas import SchemaMetaclass, Field, SchemaDefinitions

def test_schema_metaclass_inherits_fields_from_base_class():
    class BaseSchema(metaclass=SchemaMetaclass):
        base_field = Field()

    class ChildSchema(BaseSchema):
        child_field = Field()

    assert 'base_field' in ChildSchema.fields
    assert 'child_field' in ChildSchema.fields

def test_schema_metaclass_does_not_override_existing_fields():
    class BaseSchema(metaclass=SchemaMetaclass):
        base_field = Field()

    class ChildSchema(BaseSchema):
        base_field = Field()
        child_field = Field()

    assert 'base_field' in ChildSchema.fields
    assert 'child_field' in ChildSchema.fields
    assert len(ChildSchema.fields) == 2

@pytest.fixture
def mock_definitions(mocker):
    return mocker.patch('typesystem.schemas.SchemaDefinitions', new_callable=MagicMock)

def test_schema_metaclass_with_definitions(mock_definitions):
    class BaseSchema(metaclass=SchemaMetaclass):
        base_field = Field()

    class ChildSchema(BaseSchema, definitions=mock_definitions):
        child_field = Field()

    assert 'base_field' in ChildSchema.fields
    assert 'child_field' in ChildSchema.fields
    mock_definitions.__setitem__.assert_called_with('ChildSchema', ChildSchema)
