# file: typesystem/schemas.py:142-148
# asked: {"lines": [146, 147, 148], "branches": []}
# gained: {"lines": [146, 147, 148], "branches": []}

import pytest
from typesystem.schemas import Schema, SchemaMetaclass
from typesystem.fields import String

class TestSchema(Schema, metaclass=SchemaMetaclass):
    name = String()

def test_schema_validate():
    schema_instance = TestSchema.validate({"name": "example"}, strict=True)
    assert isinstance(schema_instance, TestSchema)
    assert schema_instance["name"] == "example"

    schema_instance = TestSchema.validate({"name": "example"}, strict=False)
    assert isinstance(schema_instance, TestSchema)
    assert schema_instance["name"] == "example"
