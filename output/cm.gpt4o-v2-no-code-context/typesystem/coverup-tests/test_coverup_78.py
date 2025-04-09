# file: typesystem/schemas.py:204-247
# asked: {"lines": [219, 220, 224, 225, 226, 230, 231, 232, 233, 234, 235, 238, 239, 240, 241, 242, 245, 246, 247], "branches": [[216, 219], [224, 225], [224, 226], [230, 231], [230, 235], [238, 239], [238, 240], [240, 241], [240, 242], [245, 246], [245, 247]]}
# gained: {"lines": [219, 220, 224, 225, 226, 230, 231, 232, 233, 234, 235, 238, 239, 240, 241, 242, 245, 246, 247], "branches": [[216, 219], [224, 225], [224, 226], [230, 231], [230, 235], [238, 239], [238, 240], [240, 241], [240, 242], [245, 246], [245, 247]]}

import pytest
from typesystem.schemas import Reference, Schema, Field

class DummySchema(Schema):
    pass

def test_reference_init_with_str():
    ref = Reference(to="DummySchema")
    assert ref.to == "DummySchema"
    assert ref._target_string == "DummySchema"

def test_reference_init_with_schema():
    ref = Reference(to=DummySchema)
    assert ref.to == DummySchema
    assert ref._target == DummySchema

def test_reference_target_string():
    ref = Reference(to=DummySchema)
    assert ref.target_string == "DummySchema"

    ref = Reference(to="DummySchema", definitions={"DummySchema": DummySchema})
    assert ref.target_string == "DummySchema"

def test_reference_target():
    ref = Reference(to=DummySchema)
    assert ref.target == DummySchema

    ref = Reference(to="DummySchema", definitions={"DummySchema": DummySchema})
    assert ref.target == DummySchema

    with pytest.raises(AssertionError, match="String reference missing 'definitions'."):
        ref = Reference(to="DummySchema")
        _ = ref.target

def test_reference_validate():
    ref = Reference(to=DummySchema, allow_null=True)
    assert ref.validate(None) is None

    ref = Reference(to=DummySchema, allow_null=False)
    with pytest.raises(Exception) as exc_info:
        ref.validate(None)
    assert str(exc_info.value) == "May not be null."

    ref = Reference(to=DummySchema)
    value = DummySchema()
    assert ref.validate(value) == value

def test_reference_serialize():
    ref = Reference(to=DummySchema)
    assert ref.serialize(None) is None

    obj = DummySchema()
    assert ref.serialize(obj) == dict(obj)
