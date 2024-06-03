# file typesystem/formats.py:157-171
# lines [157, 158, 160, 161, 163, 164, 165, 166, 168, 170, 171]
# branches ['165->166', '165->168']

import pytest
import uuid
import re
from typesystem.formats import UUIDFormat
from typesystem.base import ValidationError

UUID_REGEX = re.compile(
    r'^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[1-5][a-fA-F0-9]{3}-[89abAB][a-fA-F0-9]{3}-[a-fA-F0-9]{12}$'
)

def test_uuid_format_is_native_type():
    format = UUIDFormat()
    assert format.is_native_type(uuid.uuid4()) is True
    assert format.is_native_type("not-a-uuid") is False

def test_uuid_format_validate():
    format = UUIDFormat()
    valid_uuid = str(uuid.uuid4())
    assert format.validate(valid_uuid) == uuid.UUID(valid_uuid)
    
    with pytest.raises(ValidationError) as excinfo:
        format.validate("not-a-uuid")
    assert str(excinfo.value) == "Must be valid UUID format."

def test_uuid_format_serialize():
    format = UUIDFormat()
    valid_uuid = uuid.uuid4()
    assert format.serialize(valid_uuid) == str(valid_uuid)
