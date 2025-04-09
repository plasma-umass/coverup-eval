# file typesystem/schemas.py:160-164
# lines [160, 161, 164]
# branches []

import pytest
from typesystem import Schema, fields

# Define a minimal subclass of Schema for testing purposes
class TestSchema(Schema):
    field1 = fields.Integer()
    field2 = fields.String()

# Define a test case to cover the is_sparse property
def test_schema_is_sparse():
    # Create an instance of the TestSchema without any attributes set
    schema_without_attrs = TestSchema()
    assert schema_without_attrs.is_sparse is True

    # Dynamically add attributes to the schema instance to cover the other branch
    schema_with_attrs = TestSchema()
    schema_with_attrs.field1 = 123
    schema_with_attrs.field2 = 'test'
    assert schema_with_attrs.is_sparse is False  # Not sparse anymore, all fields are set as attributes
