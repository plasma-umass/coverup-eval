# file typesystem/fields.py:316-353
# lines [316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 329, 331, 332, 333, 335, 336, 338, 339, 340, 342, 343, 345, 346, 348, 349, 350, 351, 353]
# branches ['332->333', '332->335', '335->336', '335->338', '338->339', '338->353', '339->340', '339->342', '342->343', '342->345', '345->346', '345->348']

import pytest
from typesystem import ValidationError
from typesystem.fields import Boolean

@pytest.fixture
def boolean_field():
    return Boolean()

@pytest.fixture
def boolean_field_nullable():
    return Boolean(allow_null=True)

def test_boolean_field_validation(boolean_field):
    assert boolean_field.validate(True) is True
    assert boolean_field.validate(False) is False
    with pytest.raises(ValidationError) as exc_info:
        boolean_field.validate(None)
    assert str(exc_info.value) == "May not be null."

def test_boolean_field_validation_strict(boolean_field):
    with pytest.raises(ValidationError) as exc_info:
        boolean_field.validate("true", strict=True)
    assert str(exc_info.value) == "Must be a boolean."

def test_boolean_field_validation_coerce(boolean_field):
    assert boolean_field.validate("true") is True
    assert boolean_field.validate("false") is False
    assert boolean_field.validate("on") is True
    assert boolean_field.validate("off") is False
    assert boolean_field.validate("1") is True
    assert boolean_field.validate("0") is False
    assert boolean_field.validate("") is False
    assert boolean_field.validate(1) is True
    assert boolean_field.validate(0) is False

def test_boolean_field_validation_coerce_error(boolean_field):
    with pytest.raises(ValidationError) as exc_info:
        boolean_field.validate("not a boolean")
    assert str(exc_info.value) == "Must be a boolean."

def test_boolean_field_nullable_validation(boolean_field_nullable):
    assert boolean_field_nullable.validate(None) is None
    assert boolean_field_nullable.validate("null") is None
    assert boolean_field_nullable.validate("none") is None
    assert boolean_field_nullable.validate("") is None

def test_boolean_field_nullable_validation_error(boolean_field_nullable):
    with pytest.raises(ValidationError) as exc_info:
        boolean_field_nullable.validate("not a boolean")
    assert str(exc_info.value) == "Must be a boolean."
