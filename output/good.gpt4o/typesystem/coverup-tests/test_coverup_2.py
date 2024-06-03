# file typesystem/fields.py:390-401
# lines [390, 391, 392, 393, 394, 395, 396, 397, 398, 399]
# branches []

import pytest
from typesystem.fields import Object, Field

def test_object_field_errors():
    obj_field = Object()
    
    assert obj_field.errors["type"] == "Must be an object."
    assert obj_field.errors["null"] == "May not be null."
    assert obj_field.errors["invalid_key"] == "All object keys must be strings."
    assert obj_field.errors["required"] == "This field is required."
    assert obj_field.errors["invalid_property"] == "Invalid property name."
    assert obj_field.errors["empty"] == "Must not be empty."
    assert obj_field.errors["max_properties"] == "Must have no more than {max_properties} properties."
    assert obj_field.errors["min_properties"] == "Must have at least {min_properties} properties."

@pytest.fixture(autouse=True)
def cleanup(mocker):
    yield
    mocker.stopall()
