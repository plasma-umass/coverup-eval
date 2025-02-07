# file: typesystem/schemas.py:204-247
# asked: {"lines": [233, 242], "branches": [[240, 242]]}
# gained: {"lines": [242], "branches": [[240, 242]]}

import pytest
from typesystem.schemas import Reference, Schema
from typesystem.fields import Field

class DummySchema(Schema):
    pass

def test_reference_target_string_missing_definitions():
    definitions = {"DummySchema": DummySchema}
    ref = Reference(to="DummySchema", definitions=definitions)
    assert ref.target == DummySchema

def test_reference_validate_null():
    ref = Reference(to=DummySchema, allow_null=True)
    assert ref.validate(None) is None

def test_reference_validate_non_null():
    class DummyField(Field):
        def validate(self, value, *, strict=False):
            return value

    definitions = {"DummySchema": DummyField()}
    ref = Reference(to="DummySchema", definitions=definitions)
    assert ref.validate("test_value") == "test_value"

def test_reference_validate_raises_error():
    ref = Reference(to=DummySchema, allow_null=False)
    with pytest.raises(Exception) as excinfo:
        ref.validate(None)
    assert str(excinfo.value) == "May not be null."
