# file: typesystem/fields.py:682-684
# asked: {"lines": [682, 683, 684], "branches": []}
# gained: {"lines": [682, 683, 684], "branches": []}

import pytest
from typesystem.fields import Date, String

def test_date_init(monkeypatch):
    # Mock the parent class's __init__ method to track its calls
    class MockString(String):
        def __init__(self, format=None, **kwargs):
            self.format = format
            self.kwargs = kwargs
            super().__init__(**kwargs)

    monkeypatch.setattr('typesystem.fields.String', MockString)

    # Test the Date class initialization
    date_field = Date(title="Test Date")

    # Assertions to verify the correct behavior
    assert date_field.format == "date"
    assert date_field.title == "Test Date"
