# file typesystem/fields.py:78-79
# lines [78, 79]
# branches []

import pytest
from typesystem.fields import Field

class CustomField(Field):
    def __init__(self):
        self.errors = {
            'custom_error': 'Custom error with value {custom_value}'
        }
        self.custom_value = 'example'

def test_get_error_text():
    field = CustomField()
    error_text = field.get_error_text('custom_error')
    assert error_text == 'Custom error with value example'

# Cleanup is not necessary in this case as we are not modifying any shared state
