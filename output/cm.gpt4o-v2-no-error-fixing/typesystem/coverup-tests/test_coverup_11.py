# file: typesystem/formats.py:157-171
# asked: {"lines": [157, 158, 160, 161, 163, 164, 165, 166, 168, 170, 171], "branches": [[165, 166], [165, 168]]}
# gained: {"lines": [157, 158, 160, 161, 163, 164, 165, 166, 168, 170, 171], "branches": [[165, 166], [165, 168]]}

import pytest
import uuid
from typesystem.formats import UUIDFormat

def test_is_native_type():
    format = UUIDFormat()
    assert format.is_native_type(uuid.uuid4()) is True
    assert format.is_native_type("not-a-uuid") is False

def test_validate():
    format = UUIDFormat()
    valid_uuid = str(uuid.uuid4())
    assert format.validate(valid_uuid) == uuid.UUID(valid_uuid)
    
    with pytest.raises(Exception) as excinfo:
        format.validate("not-a-uuid")
    assert "Must be valid UUID format." in str(excinfo.value)

def test_serialize():
    format = UUIDFormat()
    valid_uuid = uuid.uuid4()
    assert format.serialize(valid_uuid) == str(valid_uuid)
