# file typesystem/schemas.py:92-94
# lines [92, 93]
# branches []

import pytest
from typesystem import Schema, Field

# Assuming the Schema class is part of a larger module `typesystem.schemas`
# and that the `Field` class is correctly imported from `typesystem.fields`

class DummyField(Field):
    def validate(self, value, *, strict=False):
        return value

@pytest.fixture
def cleanup_fields():
    # Fixture to clean up the class-level 'fields' attribute after each test
    yield
    Schema.fields = {}

def test_schema_fields_access(cleanup_fields):
    # Test to ensure that the Schema class can access and modify 'fields' attribute
    class MySchema(Schema):
        name = DummyField()

    assert 'name' in MySchema.fields
    assert isinstance(MySchema.fields['name'], DummyField)

    # Cleanup is handled by the cleanup_fields fixture
