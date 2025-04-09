# file: pypara/monetary.py:1196-1202
# asked: {"lines": [1196, 1198, 1199, 1200, 1201, 1202], "branches": []}
# gained: {"lines": [1196, 1198, 1199, 1200, 1201, 1202], "branches": []}

import pytest
from decimal import Decimal, DivisionByZero, InvalidOperation
from pypara.monetary import SomePrice, NoPrice
from pypara.commons.numbers import Numeric

class MockCurrency:
    def __init__(self, code):
        self.code = code

    def __eq__(self, other):
        return isinstance(other, MockCurrency) and self.code == other.code

class MockDate:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __eq__(self, other):
        return (
            isinstance(other, MockDate) and
            self.year == other.year and
            self.month == other.month and
            self.day == other.day
        )

def test_someprice_divide_by_decimal():
    price = SomePrice(MockCurrency('USD'), Decimal('100.00'), MockDate(2023, 10, 1))
    result = price.divide(Decimal('2'))
    assert result == SomePrice(MockCurrency('USD'), Decimal('50.00'), MockDate(2023, 10, 1))

def test_someprice_divide_by_int():
    price = SomePrice(MockCurrency('USD'), Decimal('100.00'), MockDate(2023, 10, 1))
    result = price.divide(2)
    assert result == SomePrice(MockCurrency('USD'), Decimal('50.00'), MockDate(2023, 10, 1))

def test_someprice_divide_by_float():
    price = SomePrice(MockCurrency('USD'), Decimal('100.00'), MockDate(2023, 10, 1))
    result = price.divide(2.0)
    assert result == SomePrice(MockCurrency('USD'), Decimal('50.00'), MockDate(2023, 10, 1))

def test_someprice_divide_by_zero():
    price = SomePrice(MockCurrency('USD'), Decimal('100.00'), MockDate(2023, 10, 1))
    result = price.divide(0)
    assert result == NoPrice

def test_someprice_divide_by_invalid_operation():
    price = SomePrice(MockCurrency('USD'), Decimal('100.00'), MockDate(2023, 10, 1))
    result = price.divide('invalid')
    assert result == NoPrice
