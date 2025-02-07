# file: typesystem/schemas.py:142-148
# asked: {"lines": [146, 147, 148], "branches": []}
# gained: {"lines": [146, 147, 148], "branches": []}

import pytest
from typesystem.schemas import Schema
from typesystem.fields import String

class TestSchema(Schema):
    name = String()

def test_schema_validate():
    schema_instance = TestSchema.validate({"name": "example"}, strict=True)
    assert isinstance(schema_instance, TestSchema)
    assert schema_instance["name"] == "example"

    with pytest.raises(Exception):
        TestSchema.validate({"name": 123}, strict=True)
