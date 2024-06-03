# file typesystem/fields.py:692-694
# lines [694]
# branches []

import pytest
from typesystem.fields import DateTime

def test_datetime_field_initialization():
    # Create an instance of DateTime with additional kwargs
    datetime_field = DateTime()

    # Assertions to verify the postconditions
    assert datetime_field.format == "datetime"
