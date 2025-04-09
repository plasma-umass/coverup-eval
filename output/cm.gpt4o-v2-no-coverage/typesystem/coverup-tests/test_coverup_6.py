# file: typesystem/formats.py:157-171
# asked: {"lines": [157, 158, 160, 161, 163, 164, 165, 166, 168, 170, 171], "branches": [[165, 166], [165, 168]]}
# gained: {"lines": [157, 158, 160, 161, 163, 164, 165, 166, 168, 170, 171], "branches": [[165, 166], [165, 168]]}

import pytest
import uuid
from typesystem.formats import UUIDFormat

class TestUUIDFormat:
    def test_is_native_type(self):
        format = UUIDFormat()
        assert format.is_native_type(uuid.uuid4()) is True
        assert format.is_native_type("not-a-uuid") is False

    def test_validate(self, monkeypatch):
        format = UUIDFormat()
        
        # Mocking UUID_REGEX to match a valid UUID
        class MockUUIDRegex:
            @staticmethod
            def match(value):
                return value == "12345678-1234-5678-1234-567812345678"
        
        monkeypatch.setattr("typesystem.formats.UUID_REGEX", MockUUIDRegex)
        
        # Valid UUID
        valid_uuid = "12345678-1234-5678-1234-567812345678"
        assert format.validate(valid_uuid) == uuid.UUID(valid_uuid)
        
        # Invalid UUID
        with pytest.raises(Exception) as excinfo:
            format.validate("invalid-uuid")
        assert "Must be valid UUID format." in str(excinfo.value)

    def test_serialize(self):
        format = UUIDFormat()
        test_uuid = uuid.uuid4()
        assert format.serialize(test_uuid) == str(test_uuid)
