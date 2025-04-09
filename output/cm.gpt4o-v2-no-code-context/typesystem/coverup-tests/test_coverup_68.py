# file: typesystem/fields.py:356-387
# asked: {"lines": [369, 370, 371, 372, 374, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387], "branches": [[377, 378], [377, 379], [379, 380], [379, 381], [381, 382], [381, 387], [382, 383], [382, 386], [383, 384], [383, 385]]}
# gained: {"lines": [369, 370, 371, 372, 374, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387], "branches": [[377, 378], [377, 379], [379, 380], [379, 381], [381, 382], [381, 387], [382, 383], [382, 386], [383, 384], [383, 385]]}

import pytest
from typesystem.fields import Choice, Field, Uniqueness

def test_choice_field_initialization():
    choices = ['a', 'b', ('c', 'C')]
    field = Choice(choices=choices)
    assert field.choices == [('a', 'a'), ('b', 'b'), ('c', 'C')]

def test_choice_field_initialization_with_invalid_choices():
    with pytest.raises(AssertionError):
        Choice(choices=['a', 'b', ('c',)])

def test_choice_field_validate_null_allowed():
    field = Choice(choices=['a', 'b'], allow_null=True)
    assert field.validate(None) is None

def test_choice_field_validate_null_not_allowed():
    field = Choice(choices=['a', 'b'], allow_null=False)
    with pytest.raises(field.validation_error("null").__class__) as exc_info:
        field.validate(None)
    assert str(exc_info.value) == "May not be null."

def test_choice_field_validate_invalid_choice():
    field = Choice(choices=['a', 'b'])
    with pytest.raises(field.validation_error("choice").__class__) as exc_info:
        field.validate('c')
    assert str(exc_info.value) == "Not a valid choice."

def test_choice_field_validate_empty_string_allowed():
    field = Choice(choices=['a', 'b'], allow_null=True)
    assert field.validate('') is None

def test_choice_field_validate_empty_string_not_allowed():
    field = Choice(choices=['a', 'b'], allow_null=False)
    with pytest.raises(field.validation_error("required").__class__) as exc_info:
        field.validate('')
    assert str(exc_info.value) == "This field is required."

def test_choice_field_validate_valid_choice():
    field = Choice(choices=['a', 'b'])
    assert field.validate('a') == 'a'
