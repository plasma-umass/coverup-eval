# file typesystem/schemas.py:204-247
# lines [219, 220, 224, 225, 226, 230, 231, 232, 233, 234, 235, 238, 239, 240, 241, 242, 245, 246, 247]
# branches ['216->219', '224->225', '224->226', '230->231', '230->235', '238->239', '238->240', '240->241', '240->242', '245->246', '245->247']

import pytest
from typesystem.schemas import Reference, Schema, Field

class DummySchema(Schema):
    pass

def test_reference_class():
    # Test for lines 219-220
    ref = Reference(to=DummySchema)
    assert ref._target == DummySchema

    # Test for lines 224-226
    ref = Reference(to=DummySchema)
    assert ref.target_string == "DummySchema"

    # Test for lines 230-235
    definitions = {"DummySchema": DummySchema}
    ref = Reference(to="DummySchema", definitions=definitions)
    assert ref.target == DummySchema

    # Test for lines 238-242
    ref = Reference(to=DummySchema, allow_null=True)
    assert ref.validate(None) is None

    ref = Reference(to=DummySchema, allow_null=False)
    with pytest.raises(Exception) as exc_info:
        ref.validate(None)
    assert str(exc_info.value) == "May not be null."

    # Test for lines 245-247
    ref = Reference(to=DummySchema)
    assert ref.serialize(None) is None
    assert ref.serialize({"key": "value"}) == {"key": "value"}
