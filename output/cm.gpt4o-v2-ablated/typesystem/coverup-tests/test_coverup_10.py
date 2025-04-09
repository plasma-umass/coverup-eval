# file: typesystem/json_schema.py:565-569
# asked: {"lines": [565, 566, 567, 568, 569], "branches": [[567, 568], [567, 569]]}
# gained: {"lines": [565, 566, 567, 568, 569], "branches": [[567, 568], [567, 569]]}

import pytest
from typesystem import Field

def test_get_standard_properties_with_default(monkeypatch):
    class MockField:
        def has_default(self):
            return True
        @property
        def default(self):
            return "default_value"

    field = MockField()
    from typesystem.json_schema import get_standard_properties
    result = get_standard_properties(field)
    assert result == {"default": "default_value"}

def test_get_standard_properties_without_default(monkeypatch):
    class MockField:
        def has_default(self):
            return False

    field = MockField()
    from typesystem.json_schema import get_standard_properties
    result = get_standard_properties(field)
    assert result == {}
