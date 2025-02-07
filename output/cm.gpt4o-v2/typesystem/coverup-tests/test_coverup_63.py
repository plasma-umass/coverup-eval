# file: typesystem/fields.py:692-694
# asked: {"lines": [692, 693, 694], "branches": []}
# gained: {"lines": [692, 693, 694], "branches": []}

import pytest
from typesystem.fields import DateTime

def test_datetime_init():
    # Create an instance of DateTime with valid kwargs
    dt = DateTime(title="Test DateTime", description="A test DateTime field", allow_null=True)
    
    # Assert that the instance is created and has the correct format
    assert dt.format == "datetime"
    assert dt.title == "Test DateTime"
    assert dt.description == "A test DateTime field"
    assert dt.allow_null is True
