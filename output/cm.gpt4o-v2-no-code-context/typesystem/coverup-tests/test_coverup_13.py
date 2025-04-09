# file: typesystem/formats.py:157-171
# asked: {"lines": [157, 158, 160, 161, 163, 164, 165, 166, 168, 170, 171], "branches": [[165, 166], [165, 168]]}
# gained: {"lines": [157, 158, 160, 161, 163, 164, 165, 166, 168, 170, 171], "branches": [[165, 166], [165, 168]]}

import pytest
import uuid
from typesystem.formats import UUIDFormat
from typesystem.base import ValidationError

def test_uuid_format_is_native_type():
    uuid_format = UUIDFormat()
    assert uuid_format.is_native_type(uuid.uuid4()) is True
    assert uuid_format.is_native_type("not-a-uuid") is False

def test_uuid_format_validate_valid_uuid():
    uuid_format = UUIDFormat()
    valid_uuid = str(uuid.uuid4())
    result = uuid_format.validate(valid_uuid)
    assert isinstance(result, uuid.UUID)
    assert str(result) == valid_uuid

def test_uuid_format_validate_invalid_uuid():
    uuid_format = UUIDFormat()
    invalid_uuid = "not-a-uuid"
    with pytest.raises(ValidationError) as excinfo:
        uuid_format.validate(invalid_uuid)
    assert "Must be valid UUID format." in str(excinfo.value)

def test_uuid_format_serialize():
    uuid_format = UUIDFormat()
    valid_uuid = uuid.uuid4()
    result = uuid_format.serialize(valid_uuid)
    assert result == str(valid_uuid)
