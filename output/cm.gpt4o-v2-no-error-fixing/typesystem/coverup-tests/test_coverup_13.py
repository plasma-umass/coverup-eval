# file: typesystem/fields.py:206-236
# asked: {"lines": [206, 209, 210, 211, 212, 213, 214, 217, 219, 220, 221, 222, 224, 225, 227, 228, 231, 232, 233, 234, 235, 236], "branches": []}
# gained: {"lines": [206, 209, 210, 211, 212, 213, 214, 217, 219, 220, 221, 222, 224, 225, 227, 228, 231, 232, 233, 234, 235, 236], "branches": []}

import pytest
import decimal
from typesystem.fields import Number

def test_number_init_with_minimum():
    num = Number(minimum=10)
    assert num.minimum == 10
    assert num.maximum is None
    assert num.exclusive_minimum is None
    assert num.exclusive_maximum is None
    assert num.multiple_of is None
    assert num.precision is None

def test_number_init_with_maximum():
    num = Number(maximum=100)
    assert num.minimum is None
    assert num.maximum == 100
    assert num.exclusive_minimum is None
    assert num.exclusive_maximum is None
    assert num.multiple_of is None
    assert num.precision is None

def test_number_init_with_exclusive_minimum():
    num = Number(exclusive_minimum=5)
    assert num.minimum is None
    assert num.maximum is None
    assert num.exclusive_minimum == 5
    assert num.exclusive_maximum is None
    assert num.multiple_of is None
    assert num.precision is None

def test_number_init_with_exclusive_maximum():
    num = Number(exclusive_maximum=50)
    assert num.minimum is None
    assert num.maximum is None
    assert num.exclusive_minimum is None
    assert num.exclusive_maximum == 50
    assert num.multiple_of is None
    assert num.precision is None

def test_number_init_with_multiple_of():
    num = Number(multiple_of=2)
    assert num.minimum is None
    assert num.maximum is None
    assert num.exclusive_minimum is None
    assert num.exclusive_maximum is None
    assert num.multiple_of == 2
    assert num.precision is None

def test_number_init_with_precision():
    num = Number(precision='0.01')
    assert num.minimum is None
    assert num.maximum is None
    assert num.exclusive_minimum is None
    assert num.exclusive_maximum is None
    assert num.multiple_of is None
    assert num.precision == '0.01'

def test_number_init_with_all_parameters():
    num = Number(
        minimum=1,
        maximum=10,
        exclusive_minimum=0,
        exclusive_maximum=11,
        precision='0.1',
        multiple_of=1
    )
    assert num.minimum == 1
    assert num.maximum == 10
    assert num.exclusive_minimum == 0
    assert num.exclusive_maximum == 11
    assert num.multiple_of == 1
    assert num.precision == '0.1'
