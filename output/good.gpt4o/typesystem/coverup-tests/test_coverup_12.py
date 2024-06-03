# file typesystem/fields.py:95-105
# lines [95, 96, 97, 98, 99, 100, 101, 102, 103]
# branches []

import pytest
from typesystem.fields import Field

class TestStringField:
    def test_string_field_errors(self):
        class String(Field):
            errors = {
                "type": "Must be a string.",
                "null": "May not be null.",
                "blank": "Must not be blank.",
                "max_length": "Must have no more than {max_length} characters.",
                "min_length": "Must have at least {min_length} characters.",
                "pattern": "Must match the pattern /{pattern}/.",
                "format": "Must be a valid {format}.",
            }

        string_field = String()

        assert string_field.errors["type"] == "Must be a string."
        assert string_field.errors["null"] == "May not be null."
        assert string_field.errors["blank"] == "Must not be blank."
        assert string_field.errors["max_length"] == "Must have no more than {max_length} characters."
        assert string_field.errors["min_length"] == "Must have at least {min_length} characters."
        assert string_field.errors["pattern"] == "Must match the pattern /{pattern}/."
        assert string_field.errors["format"] == "Must be a valid {format}."
