# file: typesystem/fields.py:682-684
# asked: {"lines": [682, 683, 684], "branches": []}
# gained: {"lines": [682, 683, 684], "branches": []}

import pytest
from typesystem.fields import Date

def test_date_init():
    # Create an instance of Date with no additional kwargs
    date_field = Date()
    assert date_field.format == "date"

    # Create an instance of Date with additional kwargs
    date_field_with_kwargs = Date(allow_blank=True, max_length=10)
    assert date_field_with_kwargs.format == "date"
    assert date_field_with_kwargs.allow_blank is True
    assert date_field_with_kwargs.max_length == 10
