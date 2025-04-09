# file: typesystem/fields.py:301-302
# asked: {"lines": [301, 302], "branches": []}
# gained: {"lines": [301, 302], "branches": []}

import pytest
from typesystem.fields import Integer, Number
from typesystem.base import ValidationError

def test_integer_inheritance():
    # Test that Integer is a subclass of Number
    assert issubclass(Integer, Number)

def test_integer_numeric_type():
    # Test that Integer has the correct numeric_type
    assert Integer.numeric_type == int

def test_integer_instance():
    # Test creating an instance of Integer and check its attributes
    integer_field = Integer(minimum=0, maximum=10)
    assert integer_field.minimum == 0
    assert integer_field.maximum == 10
    assert integer_field.numeric_type == int

def test_integer_validate():
    # Test the validate method of Integer
    integer_field = Integer(minimum=0, maximum=10)
    assert integer_field.validate(5) == 5
    with pytest.raises(ValidationError, match="Must be less than or equal to 10."):
        integer_field.validate(11)
    with pytest.raises(ValidationError, match="Must be greater than or equal to 0."):
        integer_field.validate(-1)

@pytest.fixture(autouse=True)
def cleanup(monkeypatch):
    # Cleanup code to avoid state pollution
    yield
    monkeypatch.undo()
