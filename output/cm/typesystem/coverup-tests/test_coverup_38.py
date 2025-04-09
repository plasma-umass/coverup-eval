# file typesystem/fields.py:356-387
# lines [356, 357, 358, 359, 360, 363, 366, 369, 370, 371, 372, 374, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387]
# branches ['377->378', '377->379', '379->380', '379->381', '381->382', '381->387', '382->383', '382->386', '383->384', '383->385']

import pytest
from typesystem import ValidationError
from typesystem.fields import Choice

@pytest.fixture
def choice_field():
    return Choice(choices=[('a', 'A'), 'b', ('c', 'C')])

def test_choice_field_validation(choice_field):
    # Test valid choice
    assert choice_field.validate('a') == 'a'
    
    # Test invalid choice
    with pytest.raises(ValidationError) as exc_info:
        choice_field.validate('invalid_choice')
    assert str(exc_info.value) == "Not a valid choice."
    
    # Test None with allow_null=True
    choice_field.allow_null = True
    assert choice_field.validate(None) is None
    
    # Test None with allow_null=False
    choice_field.allow_null = False
    with pytest.raises(ValidationError) as exc_info:
        choice_field.validate(None)
    assert str(exc_info.value) == "May not be null."
    
    # Test empty string with allow_null=True and strict=False
    choice_field.allow_null = True
    assert choice_field.validate('') is None
    
    # Test empty string with allow_null=True and strict=True
    with pytest.raises(ValidationError) as exc_info:
        choice_field.validate('', strict=True)
    assert str(exc_info.value) == "This field is required."
    
    # Test empty string with allow_null=False
    choice_field.allow_null = False
    with pytest.raises(ValidationError) as exc_info:
        choice_field.validate('')
    assert str(exc_info.value) == "This field is required."

def test_choice_field_initialization():
    # Test initialization with single string choices
    single_string_choice_field = Choice(choices=['x', 'y', 'z'])
    assert single_string_choice_field.choices == [('x', 'x'), ('y', 'y'), ('z', 'z')]
    
    # Test initialization with mixed choices
    mixed_choice_field = Choice(choices=[('a', 'A'), 'b', ('c', 'C')])
    assert mixed_choice_field.choices == [('a', 'A'), ('b', 'b'), ('c', 'C')]
    
    # Test initialization with invalid choices
    with pytest.raises(AssertionError):
        Choice(choices=[('a', 'A', 'extra'), 'b'])
