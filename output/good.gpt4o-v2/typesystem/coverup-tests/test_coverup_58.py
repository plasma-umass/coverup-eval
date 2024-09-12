# file: typesystem/fields.py:301-302
# asked: {"lines": [301, 302], "branches": []}
# gained: {"lines": [301, 302], "branches": []}

import pytest
from typesystem.fields import Integer

def test_integer_class():
    # Create an instance of Integer
    integer_field = Integer()

    # Check if the numeric_type is set to int
    assert integer_field.numeric_type == int
