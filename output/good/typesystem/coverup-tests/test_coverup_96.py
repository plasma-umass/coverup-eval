# file typesystem/schemas.py:189-190
# lines [190]
# branches []

import pytest
from typesystem import Schema, fields

class MyTestSchema(Schema):
    field1 = fields.String()
    field2 = fields.Integer()

@pytest.fixture
def cleanup_schema_fields():
    # Fixture to cleanup any class-level modifications after the test
    original_fields = MyTestSchema.fields.copy()
    yield
    MyTestSchema.fields = original_fields

def test_schema_len(mocker, cleanup_schema_fields):
    # Mocking `hasattr` to control the behavior and ensure the line is executed
    mocker.patch('typesystem.schemas.hasattr', return_value=True)
    schema_instance = MyTestSchema()
    assert len(schema_instance) == 2  # Assuming both fields should be counted
