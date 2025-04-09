# file: typesystem/fields.py:682-684
# asked: {"lines": [682, 683, 684], "branches": []}
# gained: {"lines": [682, 683, 684], "branches": []}

import pytest
from typesystem.fields import Date

def test_date_initialization():
    # Test that the Date class initializes correctly with the format set to 'date'
    date_field = Date()
    assert date_field.format == 'date'

    # Test that additional kwargs are passed correctly
    date_field_with_kwargs = Date(title="Birthdate", description="The birthdate of the user")
    assert date_field_with_kwargs.title == "Birthdate"
    assert date_field_with_kwargs.description == "The birthdate of the user"
