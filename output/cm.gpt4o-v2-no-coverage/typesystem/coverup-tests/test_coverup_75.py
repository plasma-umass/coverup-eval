# file: typesystem/fields.py:687-689
# asked: {"lines": [687, 688, 689], "branches": []}
# gained: {"lines": [687, 688, 689], "branches": []}

import pytest
from typesystem.fields import Time

def test_time_init(monkeypatch):
    # Mock the parent class's __init__ method to ensure it is called with the correct parameters
    class MockString:
        def __init__(self, *, allow_blank=False, trim_whitespace=True, max_length=None, min_length=None, pattern=None, format=None, title='', description='', default=None, allow_null=False):
            self.allow_blank = allow_blank
            self.trim_whitespace = trim_whitespace
            self.max_length = max_length
            self.min_length = min_length
            self.pattern = pattern
            self.format = format
            self.title = title
            self.description = description
            self.default = default
            self.allow_null = allow_null

    monkeypatch.setattr('typesystem.fields.String', MockString)

    # Create an instance of Time with additional keyword arguments
    time_instance = Time(allow_blank=True, title='Test Title')

    # Assertions to verify the correct behavior
    assert time_instance.format == 'time'
    assert time_instance.title == 'Test Title'
    assert time_instance.allow_blank is True
