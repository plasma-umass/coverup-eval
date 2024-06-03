# file typesystem/fields.py:682-684
# lines [682, 683, 684]
# branches []

import pytest
import typing
from typesystem.fields import String

class Date(String):
    def __init__(self, **kwargs: typing.Any) -> None:
        super().__init__(format="date", **kwargs)

def test_date_field_initialization():
    # Test initialization with no additional kwargs
    date_field = Date()
    assert date_field.format == "date"
    
    # Test initialization with additional kwargs
    date_field_with_kwargs = Date(title="Birthdate", description="The date of birth")
    assert date_field_with_kwargs.format == "date"
    assert date_field_with_kwargs.title == "Birthdate"
    assert date_field_with_kwargs.description == "The date of birth"
