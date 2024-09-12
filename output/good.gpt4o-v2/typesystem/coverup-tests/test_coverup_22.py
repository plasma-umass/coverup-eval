# file: typesystem/schemas.py:204-247
# asked: {"lines": [204, 205, 207, 210, 213, 214, 215, 216, 217, 219, 220, 222, 223, 224, 225, 226, 228, 229, 230, 231, 232, 233, 234, 235, 237, 238, 239, 240, 241, 242, 244, 245, 246, 247], "branches": [[216, 217], [216, 219], [224, 225], [224, 226], [230, 231], [230, 235], [238, 239], [238, 240], [240, 241], [240, 242], [245, 246], [245, 247]]}
# gained: {"lines": [204, 205, 207, 210, 213, 214, 215, 216, 217, 219, 220, 222, 223, 224, 225, 226, 228, 229, 230, 231, 232, 234, 235, 237, 238, 239, 240, 241, 244, 245, 246, 247], "branches": [[216, 217], [216, 219], [224, 225], [224, 226], [230, 231], [230, 235], [238, 239], [238, 240], [240, 241], [245, 246], [245, 247]]}

import pytest
from typesystem.schemas import Reference, Schema
from typesystem.fields import Field
from typesystem.base import ValidationError

class ExampleSchema(Schema):
    pass

def test_reference_init_with_string():
    ref = Reference(to="ExampleSchema", definitions={"ExampleSchema": ExampleSchema})
    assert ref.to == "ExampleSchema"
    assert ref.definitions == {"ExampleSchema": ExampleSchema}
    assert ref._target_string == "ExampleSchema"

def test_reference_init_with_type():
    ref = Reference(to=ExampleSchema)
    assert ref.to == ExampleSchema
    assert ref._target == ExampleSchema

def test_reference_target_string():
    ref = Reference(to=ExampleSchema)
    assert ref.target_string == "ExampleSchema"

    ref = Reference(to="ExampleSchema", definitions={"ExampleSchema": ExampleSchema})
    assert ref.target_string == "ExampleSchema"

def test_reference_target():
    ref = Reference(to=ExampleSchema)
    assert ref.target == ExampleSchema

    ref = Reference(to="ExampleSchema", definitions={"ExampleSchema": ExampleSchema})
    assert ref.target == ExampleSchema

def test_reference_validate():
    ref = Reference(to=ExampleSchema)
    with pytest.raises(ValidationError):
        ref.validate(None)

    ref.allow_null = True
    assert ref.validate(None) is None

def test_reference_serialize():
    ref = Reference(to=ExampleSchema)
    assert ref.serialize(None) is None
    assert ref.serialize({"key": "value"}) == {"key": "value"}
