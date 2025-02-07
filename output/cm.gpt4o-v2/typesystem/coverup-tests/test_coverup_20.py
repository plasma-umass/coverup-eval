# file: typesystem/fields.py:356-387
# asked: {"lines": [356, 357, 358, 359, 360, 363, 366, 369, 370, 371, 372, 374, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387], "branches": [[377, 378], [377, 379], [379, 380], [379, 381], [381, 382], [381, 387], [382, 383], [382, 386], [383, 384], [383, 385]]}
# gained: {"lines": [356, 357, 358, 359, 360, 363, 366, 369, 370, 371, 372, 374, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387], "branches": [[377, 378], [377, 379], [379, 380], [379, 381], [381, 382], [381, 387], [382, 383], [382, 386], [383, 384], [383, 385]]}

import pytest
from typesystem.fields import Choice
from typesystem.base import ValidationError

def test_choice_init_with_valid_choices():
    choices = ['a', 'b', ('c', 'C')]
    field = Choice(choices=choices)
    assert field.choices == [('a', 'a'), ('b', 'b'), ('c', 'C')]

def test_choice_init_with_invalid_choices():
    with pytest.raises(AssertionError):
        Choice(choices=[('a',)])

def test_choice_validate_with_none_value_and_allow_null(monkeypatch):
    field = Choice(choices=['a', 'b'])
    monkeypatch.setattr(field, 'allow_null', True)
    assert field.validate(None) is None

def test_choice_validate_with_none_value_and_not_allow_null(monkeypatch):
    field = Choice(choices=['a', 'b'])
    monkeypatch.setattr(field, 'allow_null', False)
    with pytest.raises(ValidationError) as excinfo:
        field.validate(None)
    assert str(excinfo.value) == "May not be null."

def test_choice_validate_with_invalid_choice():
    field = Choice(choices=['a', 'b'])
    with pytest.raises(ValidationError) as excinfo:
        field.validate('c')
    assert str(excinfo.value) == "Not a valid choice."

def test_choice_validate_with_empty_string_and_allow_null(monkeypatch):
    field = Choice(choices=['a', 'b'])
    monkeypatch.setattr(field, 'allow_null', True)
    assert field.validate('') is None

def test_choice_validate_with_empty_string_and_not_allow_null(monkeypatch):
    field = Choice(choices=['a', 'b'])
    monkeypatch.setattr(field, 'allow_null', False)
    with pytest.raises(ValidationError) as excinfo:
        field.validate('')
    assert str(excinfo.value) == "This field is required."

def test_choice_validate_with_valid_choice():
    field = Choice(choices=['a', 'b'])
    assert field.validate('a') == 'a'
