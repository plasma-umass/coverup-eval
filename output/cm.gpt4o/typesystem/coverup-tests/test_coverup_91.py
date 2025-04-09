# file typesystem/fields.py:356-387
# lines [377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387]
# branches ['377->378', '377->379', '379->380', '379->381', '381->382', '381->387', '382->383', '382->386', '383->384', '383->385']

import pytest
from typesystem.fields import Choice, ValidationError

def test_choice_field_validation(mocker):
    # Mocking the Uniqueness class to ensure it behaves as expected
    mocker.patch('typesystem.fields.Uniqueness', side_effect=lambda x: x)

    # Test case where value is None and allow_null is True
    field = Choice(choices=["a", "b"], allow_null=True)
    assert field.validate(None) is None

    # Test case where value is None and allow_null is False
    field = Choice(choices=["a", "b"], allow_null=False)
    with pytest.raises(ValidationError) as excinfo:
        field.validate(None)
    assert str(excinfo.value) == "May not be null."

    # Test case where value is not in choices and value is an empty string, allow_null is True, and strict is False
    field = Choice(choices=["a", "b"], allow_null=True)
    assert field.validate("") is None

    # Test case where value is not in choices and value is an empty string, allow_null is False
    field = Choice(choices=["a", "b"], allow_null=False)
    with pytest.raises(ValidationError) as excinfo:
        field.validate("")
    assert str(excinfo.value) == "This field is required."

    # Test case where value is not in choices and value is not an empty string
    field = Choice(choices=["a", "b"], allow_null=False)
    with pytest.raises(ValidationError) as excinfo:
        field.validate("c")
    assert str(excinfo.value) == "Not a valid choice."

    # Test case where value is in choices
    field = Choice(choices=["a", "b"], allow_null=False)
    assert field.validate("a") == "a"
