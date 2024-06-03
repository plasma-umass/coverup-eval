# file typesystem/fields.py:692-694
# lines [692, 693, 694]
# branches []

import pytest
import typing
from typesystem.fields import String

class DateTime(String):
    def __init__(self, **kwargs: typing.Any) -> None:
        super().__init__(format="datetime", **kwargs)

def test_datetime_field_initialization():
    # Create an instance of DateTime with additional kwargs
    datetime_field = DateTime()

    # Assertions to verify the initialization
    assert datetime_field.format == "datetime"
