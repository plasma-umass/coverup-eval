# file: typesystem/fields.py:305-306
# asked: {"lines": [305, 306], "branches": []}
# gained: {"lines": [305, 306], "branches": []}

import pytest
from typesystem.fields import Float
from typesystem.base import ValidationError

def test_float_initialization():
    # Test initialization with default parameters
    field = Float()
    assert field.numeric_type == float
    assert field.minimum is None
    assert field.maximum is None
    assert field.exclusive_minimum is None
    assert field.exclusive_maximum is None
    assert field.multiple_of is None
    assert field.precision is None

def test_float_initialization_with_parameters():
    # Test initialization with specific parameters
    field = Float(minimum=0.0, maximum=10.0, exclusive_minimum=1.0, exclusive_maximum=9.0, multiple_of=0.5, precision='0.01')
    assert field.numeric_type == float
    assert field.minimum == 0.0
    assert field.maximum == 10.0
    assert field.exclusive_minimum == 1.0
    assert field.exclusive_maximum == 9.0
    assert field.multiple_of == 0.5
    assert field.precision == '0.01'

def test_float_validation():
    # Test validation method
    field = Float(minimum=0.0, maximum=10.0)
    assert field.validate(5.0) == 5.0
    with pytest.raises(ValidationError):
        field.validate(-1.0)
    with pytest.raises(ValidationError):
        field.validate(11.0)
