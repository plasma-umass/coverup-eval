# file: typesystem/fields.py:186-189
# asked: {"lines": [187, 188, 189], "branches": [[187, 188], [187, 189]]}
# gained: {"lines": [187, 188, 189], "branches": [[187, 188], [187, 189]]}

import pytest
from typesystem.fields import String, FORMATS

class MockFormat:
    @staticmethod
    def serialize(obj):
        return f"formatted-{obj}"

@pytest.fixture
def setup_formats(monkeypatch):
    original_formats = FORMATS.copy()
    monkeypatch.setitem(FORMATS, 'mock_format', MockFormat)
    yield
    FORMATS.clear()
    FORMATS.update(original_formats)

def test_string_serialize_with_format(setup_formats):
    field = String(format='mock_format')
    result = field.serialize('test')
    assert result == 'formatted-test'

def test_string_serialize_without_format():
    field = String(format='non_existent_format')
    result = field.serialize('test')
    assert result == 'test'
