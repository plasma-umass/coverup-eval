# file typesystem/schemas.py:204-247
# lines [219, 220, 224, 225, 226, 230, 231, 232, 233, 234, 235, 238, 239, 240, 241, 242, 245, 246, 247]
# branches ['216->219', '224->225', '224->226', '230->231', '230->235', '238->239', '238->240', '240->241', '240->242', '245->246', '245->247']

import pytest
from typesystem import Schema, Field
from typesystem.schemas import Reference
from typesystem.fields import ValidationError

class DummySchema(Schema):
    pass

class TestReference:
    def test_reference_with_schema_class(self):
        ref = Reference(to=DummySchema)
        assert ref.target == DummySchema

    def test_reference_with_string_and_definitions(self):
        definitions = {'DummySchema': DummySchema}
        ref = Reference(to='DummySchema', definitions=definitions)
        assert ref.target == DummySchema
        assert ref.target_string == 'DummySchema'

    def test_reference_validation_null_allowed(self):
        ref = Reference(to=DummySchema, allow_null=True)
        assert ref.validate(None) is None

    def test_reference_validation_null_not_allowed(self):
        ref = Reference(to=DummySchema, allow_null=False)
        with pytest.raises(ValidationError):
            ref.validate(None)

    def test_reference_serialization(self):
        ref = Reference(to=DummySchema)
        obj = DummySchema()
        assert ref.serialize(obj) == dict(obj)
        assert ref.serialize(None) is None
