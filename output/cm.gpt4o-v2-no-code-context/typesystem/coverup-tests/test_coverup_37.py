# file: typesystem/fields.py:301-302
# asked: {"lines": [301, 302], "branches": []}
# gained: {"lines": [301, 302], "branches": []}

import pytest
from typesystem.fields import Number

def test_integer_class():
    class Integer(Number):
        numeric_type = int

    # Verify that the class is created and the numeric_type is set correctly
    assert Integer.numeric_type == int
