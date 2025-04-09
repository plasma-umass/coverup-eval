# file: typesystem/schemas.py:204-247
# asked: {"lines": [204, 205, 207, 210, 213, 214, 215, 216, 217, 219, 220, 222, 223, 224, 225, 226, 228, 229, 230, 231, 232, 233, 234, 235, 237, 238, 239, 240, 241, 242, 244, 245, 246, 247], "branches": [[216, 217], [216, 219], [224, 225], [224, 226], [230, 231], [230, 235], [238, 239], [238, 240], [240, 241], [240, 242], [245, 246], [245, 247]]}
# gained: {"lines": [204, 205, 207, 210, 213, 214, 215, 216, 217, 219, 220, 222, 223, 224, 225, 226, 228, 229, 230, 231, 232, 234, 235, 237, 238, 239, 240, 241, 242, 244, 245, 246, 247], "branches": [[216, 217], [216, 219], [224, 225], [224, 226], [230, 231], [230, 235], [238, 239], [238, 240], [240, 241], [240, 242], [245, 246], [245, 247]]}

import pytest
from typesystem.schemas import Field, Schema, Reference

class DummySchema(Schema):
    pass

def test_reference_init_with_schema():
    ref = Reference(to=DummySchema)
    assert ref.to == DummySchema
    assert ref._target == DummySchema
    assert ref.target == DummySchema

def test_reference_init_with_string():
    definitions = {"DummySchema": DummySchema}
    ref = Reference(to="DummySchema", definitions=definitions)
    assert ref.to == "DummySchema"
    assert ref.definitions == definitions
    assert ref._target_string == "DummySchema"
    assert ref.target == DummySchema

def test_reference_target_string_property():
    ref = Reference(to=DummySchema)
    assert ref.target_string == "DummySchema"

    definitions = {"DummySchema": DummySchema}
    ref = Reference(to="DummySchema", definitions=definitions)
    assert ref.target_string == "DummySchema"

def test_reference_target_property():
    definitions = {"DummySchema": DummySchema}
    ref = Reference(to="DummySchema", definitions=definitions)
    assert ref.target == DummySchema

def test_reference_validate():
    ref = Reference(to=DummySchema)
    with pytest.raises(Exception) as excinfo:
        ref.validate(None)
    assert str(excinfo.value) == "May not be null."

    ref.allow_null = True
    assert ref.validate(None) is None

    obj = DummySchema()
    assert ref.validate(obj) == obj

def test_reference_serialize():
    ref = Reference(to=DummySchema)
    assert ref.serialize(None) is None

    obj = DummySchema()
    assert ref.serialize(obj) == dict(obj)
