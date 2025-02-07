# file: typesystem/schemas.py:133-140
# asked: {"lines": [133, 134, 135, 136, 137, 138, 139], "branches": []}
# gained: {"lines": [133, 134, 135, 136, 137, 138, 139], "branches": []}

import pytest
from typesystem.schemas import Schema
from typesystem.fields import String, Integer, Object

class TestSchema(Schema):
    name = String()
    age = Integer(default=0)

def test_make_validator():
    validator = TestSchema.make_validator(strict=True)
    assert isinstance(validator, Object)
    assert validator.required == ['name']
    assert validator.additional_properties is False

    validator = TestSchema.make_validator(strict=False)
    assert validator.additional_properties is None

    assert 'name' in validator.properties
    assert 'age' in validator.properties
