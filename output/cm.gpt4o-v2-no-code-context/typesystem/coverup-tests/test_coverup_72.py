# file: typesystem/fields.py:238-298
# asked: {"lines": [240, 242, 244, 246, 254, 267, 270, 271, 272, 273, 274, 276, 279, 282, 285, 288, 291, 292, 293, 295, 296], "branches": [[239, 240], [241, 242], [243, 244], [245, 246], [253, 254], [260, 265], [265, 267], [269, 270], [278, 279], [281, 282], [284, 285], [287, 288], [290, 291], [291, 292], [291, 295], [292, 293], [292, 298], [295, 296], [295, 298]]}
# gained: {"lines": [240, 242, 244, 246, 254, 267, 270, 271, 272, 273, 274, 276, 279, 282, 285, 288, 291, 292, 293, 295, 296], "branches": [[239, 240], [241, 242], [243, 244], [245, 246], [253, 254], [260, 265], [265, 267], [269, 270], [278, 279], [281, 282], [284, 285], [287, 288], [290, 291], [291, 292], [291, 295], [292, 293], [295, 296]]}

import pytest
from typesystem.fields import Number
import decimal

def test_validate_allow_null():
    field = Number(allow_null=True)
    assert field.validate(None) is None
    assert field.validate("", strict=False) is None

def test_validate_null():
    field = Number(allow_null=False)
    with pytest.raises(field.validation_error("null").__class__):
        field.validate(None)

def test_validate_bool():
    field = Number()
    with pytest.raises(field.validation_error("type").__class__):
        field.validate(True)

def test_validate_strict_type():
    field = Number()
    with pytest.raises(field.validation_error("type").__class__):
        field.validate("123", strict=True)

def test_validate_non_integer_float():
    class CustomNumber(Number):
        numeric_type = int

    field = CustomNumber()
    with pytest.raises(field.validation_error("integer").__class__):
        field.validate(123.45)

def test_validate_infinite():
    field = Number()
    with pytest.raises(field.validation_error("finite").__class__):
        field.validate(float('inf'))

def test_validate_precision():
    field = Number(precision="0.01")
    assert field.validate(123.456) == 123.46

def test_validate_minimum():
    field = Number(minimum=10)
    with pytest.raises(field.validation_error("minimum").__class__):
        field.validate(5)

def test_validate_exclusive_minimum():
    field = Number(exclusive_minimum=10)
    with pytest.raises(field.validation_error("exclusive_minimum").__class__):
        field.validate(10)

def test_validate_maximum():
    field = Number(maximum=10)
    with pytest.raises(field.validation_error("maximum").__class__):
        field.validate(15)

def test_validate_exclusive_maximum():
    field = Number(exclusive_maximum=10)
    with pytest.raises(field.validation_error("exclusive_maximum").__class__):
        field.validate(10)

def test_validate_multiple_of_int():
    field = Number(multiple_of=3)
    with pytest.raises(field.validation_error("multiple_of").__class__):
        field.validate(10)

def test_validate_multiple_of_float():
    field = Number(multiple_of=0.1)
    with pytest.raises(field.validation_error("multiple_of").__class__):
        field.validate(0.15)
