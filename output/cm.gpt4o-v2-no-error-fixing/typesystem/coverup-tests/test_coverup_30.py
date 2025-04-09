# file: typesystem/fields.py:677-679
# asked: {"lines": [677, 678, 679], "branches": []}
# gained: {"lines": [677, 678, 679], "branches": []}

import pytest
from typesystem.fields import Text

def test_text_initialization():
    # Create an instance of Text with additional kwargs
    text_field = Text(allow_blank=True, max_length=100)
    
    # Assertions to verify the initialization
    assert text_field.allow_blank is True
    assert text_field.max_length == 100
    assert text_field.format == 'text'
