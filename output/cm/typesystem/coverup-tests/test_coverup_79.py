# file typesystem/schemas.py:175-182
# lines [179, 180]
# branches []

import pytest
from typesystem import Schema

# Assuming the Schema class is part of a module named typesystem.schemas
# and the file structure is as follows:
# typesystem/
# ├── __init__.py
# └── schemas.py

# Define a minimal schema for testing purposes
class TestSchema(Schema):
    pass

# Test function to cover the missing lines 179-180
def test_schema_getitem_key_error():
    test_schema = TestSchema()

    # Attempt to access a non-existent key to trigger the KeyError
    with pytest.raises(KeyError) as exc_info:
        test_schema['non_existent_key']

    # Assert that the KeyError was raised with the correct message
    assert str(exc_info.value) == "'non_existent_key'"
