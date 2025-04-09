# file: typesystem/fields.py:186-189
# asked: {"lines": [187, 188, 189], "branches": [[187, 188], [187, 189]]}
# gained: {"lines": [187, 188, 189], "branches": [[187, 188], [187, 189]]}

import pytest
from typesystem.fields import String, FORMATS

def test_string_serialize_with_format(monkeypatch):
    class MockFormat:
        @staticmethod
        def serialize(obj):
            return f"formatted-{obj}"

    mock_formats = {"mock_format": MockFormat}
    monkeypatch.setattr("typesystem.fields.FORMATS", mock_formats)

    field = String(format="mock_format")
    result = field.serialize("test")
    assert result == "formatted-test"

def test_string_serialize_without_format():
    field = String(format="non_existent_format")
    result = field.serialize("test")
    assert result == "test"
