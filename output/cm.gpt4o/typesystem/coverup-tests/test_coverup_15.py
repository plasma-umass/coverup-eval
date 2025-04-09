# file typesystem/fields.py:550-561
# lines [550, 551, 552, 553, 554, 555, 556, 557, 558, 559]
# branches []

import pytest
from typesystem.fields import Field

class TestArrayField:
    def test_array_field_errors(self):
        class Array(Field):
            errors = {
                "type": "Must be an array.",
                "null": "May not be null.",
                "empty": "Must not be empty.",
                "exact_items": "Must have {min_items} items.",
                "min_items": "Must have at least {min_items} items.",
                "max_items": "Must have no more than {max_items} items.",
                "additional_items": "May not contain additional items.",
                "unique_items": "Items must be unique.",
            }

        array_field = Array()

        assert array_field.errors["type"] == "Must be an array."
        assert array_field.errors["null"] == "May not be null."
        assert array_field.errors["empty"] == "Must not be empty."
        assert array_field.errors["exact_items"] == "Must have {min_items} items."
        assert array_field.errors["min_items"] == "Must have at least {min_items} items."
        assert array_field.errors["max_items"] == "Must have no more than {max_items} items."
        assert array_field.errors["additional_items"] == "May not contain additional items."
        assert array_field.errors["unique_items"] == "Items must be unique."
