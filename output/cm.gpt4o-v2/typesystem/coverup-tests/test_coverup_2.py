# file: typesystem/formats.py:157-171
# asked: {"lines": [157, 158, 160, 161, 163, 164, 165, 166, 168, 170, 171], "branches": [[165, 166], [165, 168]]}
# gained: {"lines": [157, 158, 160, 161, 163, 164, 165, 166, 168, 170, 171], "branches": [[165, 166], [165, 168]]}

import pytest
import uuid
from typesystem.formats import UUIDFormat, UUID_REGEX
from typesystem.base import ValidationError

def test_uuid_format_is_native_type():
    format = UUIDFormat()
    assert format.is_native_type(uuid.uuid4()) is True
    assert format.is_native_type("not-a-uuid") is False

def test_uuid_format_validate():
    format = UUIDFormat()
    valid_uuid = str(uuid.uuid4())
    assert format.validate(valid_uuid) == uuid.UUID(valid_uuid)
    
    with pytest.raises(ValidationError) as exc_info:
        format.validate("not-a-uuid")
    assert str(exc_info.value) == "Must be valid UUID format."

def test_uuid_format_serialize():
    format = UUIDFormat()
    valid_uuid = uuid.uuid4()
    assert format.serialize(valid_uuid) == str(valid_uuid)
