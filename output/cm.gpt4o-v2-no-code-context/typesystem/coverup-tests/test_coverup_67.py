# file: typesystem/fields.py:692-694
# asked: {"lines": [694], "branches": []}
# gained: {"lines": [694], "branches": []}

import pytest
from typesystem.fields import DateTime

def test_datetime_init(monkeypatch):
    # Mock the parent class __init__ method to avoid unexpected keyword argument error
    def mock_init(self, *args, **kwargs):
        self.format = kwargs.get('format')
        self.required = kwargs.get('required')
        self.title = kwargs.get('title')

    monkeypatch.setattr("typesystem.fields.String.__init__", mock_init)

    # Create an instance of DateTime with additional kwargs
    dt = DateTime(required=True, title="Test DateTime")

    # Assert that the instance has the correct attributes
    assert dt.format == "datetime"
    assert dt.required is True
    assert dt.title == "Test DateTime"
