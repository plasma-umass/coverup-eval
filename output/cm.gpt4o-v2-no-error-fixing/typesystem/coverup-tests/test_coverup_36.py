# file: typesystem/fields.py:301-302
# asked: {"lines": [301, 302], "branches": []}
# gained: {"lines": [301, 302], "branches": []}

import pytest
from typesystem.fields import Integer

def test_integer_numeric_type():
    integer_field = Integer()
    assert integer_field.numeric_type == int
