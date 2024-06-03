# file typesystem/fields.py:192-205
# lines [192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203]
# branches []

import pytest
import typing
from typesystem.fields import Field

class TestNumberField:
    def test_number_field_initialization(self):
        class Number(Field):
            numeric_type: typing.Optional[type] = None
            errors = {
                "type": "Must be a number.",
                "null": "May not be null.",
                "integer": "Must be an integer.",
                "finite": "Must be finite.",
                "minimum": "Must be greater than or equal to {minimum}.",
                "exclusive_minimum": "Must be greater than {exclusive_minimum}.",
                "maximum": "Must be less than or equal to {maximum}.",
                "exclusive_maximum": "Must be less than {exclusive_maximum}.",
                "multiple_of": "Must be a multiple of {multiple_of}.",
            }

        number_field = Number()
        assert number_field.numeric_type is None
        assert number_field.errors["type"] == "Must be a number."
        assert number_field.errors["null"] == "May not be null."
        assert number_field.errors["integer"] == "Must be an integer."
        assert number_field.errors["finite"] == "Must be finite."
        assert number_field.errors["minimum"] == "Must be greater than or equal to {minimum}."
        assert number_field.errors["exclusive_minimum"] == "Must be greater than {exclusive_minimum}."
        assert number_field.errors["maximum"] == "Must be less than or equal to {maximum}."
        assert number_field.errors["exclusive_maximum"] == "Must be less than {exclusive_maximum}."
        assert number_field.errors["multiple_of"] == "Must be a multiple of {multiple_of}."
