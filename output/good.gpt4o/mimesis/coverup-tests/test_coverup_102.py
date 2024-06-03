# file mimesis/schema.py:113-115
# lines [113, 114, 115]
# branches []

import pytest
from unittest.mock import patch

# Assuming the AbstractField class is imported from mimesis.schema
from mimesis.schema import AbstractField

def test_abstract_field_str_method():
    # Create an instance of AbstractField and set the locale attribute
    field = AbstractField()
    field.locale = 'en'
    
    result = str(field)
    assert result == 'AbstractField <en>'
