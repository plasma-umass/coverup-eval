# file: typesystem/fields.py:692-694
# asked: {"lines": [692, 693, 694], "branches": []}
# gained: {"lines": [692, 693, 694], "branches": []}

import pytest
from typesystem.fields import DateTime

def test_datetime_init():
    # Create an instance of DateTime with additional kwargs
    dt = DateTime(allow_blank=True, max_length=10)
    
    # Assertions to verify the postconditions
    assert dt.format == 'datetime'
    assert dt.allow_blank is True
    assert dt.max_length == 10

