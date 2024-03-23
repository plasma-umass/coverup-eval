# file mimesis/exceptions.py:55-67
# lines [55, 56, 58, 63, 64, 66, 67]
# branches []

import pytest
from mimesis.exceptions import UnsupportedField

def test_unsupported_field_exception():
    field_name = "test_field"
    exception = UnsupportedField(name=field_name)
    
    assert str(exception) == f'Field «{field_name}» is not supported.', "The exception message does not match the expected output."

def test_unsupported_field_exception_without_name():
    exception = UnsupportedField()
    
    assert str(exception) == 'Field «None» is not supported.', "The exception message does not match the expected output when no name is provided."
