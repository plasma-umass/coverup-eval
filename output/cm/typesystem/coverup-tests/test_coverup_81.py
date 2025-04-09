# file typesystem/fields.py:68-72
# lines [69, 70, 71, 72]
# branches ['70->71', '70->72']

import pytest
from typesystem.fields import Field

def test_field_get_default_value_callable():
    class TestField(Field):
        default = staticmethod(lambda: "callable_default")

    field = TestField()
    assert field.get_default_value() == "callable_default"

def test_field_get_default_value_non_callable():
    class TestField(Field):
        default = "non_callable_default"

    field = TestField()
    assert field.get_default_value() == "non_callable_default"
