# file typesystem/formats.py:157-171
# lines [161, 164, 165, 166, 168, 171]
# branches ['165->166', '165->168']

import pytest
import uuid
from typesystem import ValidationError
from typesystem.formats import UUIDFormat

@pytest.fixture
def uuid_format():
    return UUIDFormat()

def test_uuid_format_validation(uuid_format):
    valid_uuid = str(uuid.uuid4())
    invalid_uuid = 'invalid-uuid-string'

    # Test valid UUID
    assert isinstance(uuid_format.validate(valid_uuid), uuid.UUID)

    # Test invalid UUID
    with pytest.raises(ValidationError) as exc_info:
        uuid_format.validate(invalid_uuid)
    assert "Must be valid UUID format." in str(exc_info.value)

def test_uuid_format_is_native_type(uuid_format):
    valid_uuid_obj = uuid.uuid4()
    invalid_uuid_obj = 'not-a-uuid-object'

    # Test with actual UUID object
    assert uuid_format.is_native_type(valid_uuid_obj) is True

    # Test with non-UUID object
    assert uuid_format.is_native_type(invalid_uuid_obj) is False

def test_uuid_format_serialize(uuid_format):
    valid_uuid_obj = uuid.uuid4()

    # Test serialization
    assert uuid_format.serialize(valid_uuid_obj) == str(valid_uuid_obj)
