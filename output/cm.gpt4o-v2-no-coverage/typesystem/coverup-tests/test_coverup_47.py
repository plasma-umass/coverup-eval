# file: typesystem/schemas.py:142-148
# asked: {"lines": [142, 143, 144, 146, 147, 148], "branches": []}
# gained: {"lines": [142, 143, 144, 146, 147, 148], "branches": []}

import pytest
from typesystem.schemas import Schema
from typesystem.fields import Field, String
from typesystem.base import ValidationError

class TestSchema(Schema):
    name = String(max_length=100)
    email = String(max_length=100)

def test_schema_validate():
    data = {"name": "John Doe", "email": "john.doe@example.com"}
    schema_instance = TestSchema.validate(data)
    assert isinstance(schema_instance, TestSchema)
    assert schema_instance.name == "John Doe"
    assert schema_instance.email == "john.doe@example.com"

def test_schema_validate_strict():
    data = {"name": "John Doe", "email": "john.doe@example.com"}
    schema_instance = TestSchema.validate(data, strict=True)
    assert isinstance(schema_instance, TestSchema)
    assert schema_instance.name == "John Doe"
    assert schema_instance.email == "john.doe@example.com"

def test_schema_validate_invalid():
    data = {"name": "John Doe"}
    with pytest.raises(ValidationError):
        TestSchema.validate(data)

def test_schema_validate_extra_field():
    data = {"name": "John Doe", "email": "john.doe@example.com", "extra": "field"}
    with pytest.raises(ValidationError):
        TestSchema.validate(data, strict=True)
