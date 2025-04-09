# file: typesystem/fields.py:78-79
# asked: {"lines": [78, 79], "branches": []}
# gained: {"lines": [78, 79], "branches": []}

import pytest
from typesystem.fields import Field

class TestField:
    def test_get_error_text(self, monkeypatch):
        # Create a mock Field instance with a specific error dictionary
        field = Field()
        monkeypatch.setattr(field, 'errors', {'required': 'This field is required.'})
        monkeypatch.setattr(field, '__dict__', {'name': 'test_field', 'errors': {'required': 'This field is required.'}})

        # Call the method and assert the expected result
        error_text = field.get_error_text('required')
        assert error_text == 'This field is required.'

    def test_get_error_text_with_formatting(self, monkeypatch):
        # Create a mock Field instance with a specific error dictionary
        field = Field()
        monkeypatch.setattr(field, 'errors', {'invalid': 'The field {name} is invalid.'})
        monkeypatch.setattr(field, '__dict__', {'name': 'test_field', 'errors': {'invalid': 'The field {name} is invalid.'}})

        # Call the method and assert the expected result
        error_text = field.get_error_text('invalid')
        assert error_text == 'The field test_field is invalid.'
