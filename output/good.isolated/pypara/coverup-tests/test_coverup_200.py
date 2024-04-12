# file pypara/monetary.py:421-422
# lines [421, 422]
# branches []

import pytest
from decimal import Decimal
from datetime import date
from pypara.monetary import SomeMoney, Currency

class FakeCurrency:
    def __init__(self, code):
        self.code = code

    def __eq__(self, other):
        return self.code == other.code

class FakeDate:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def today(cls):
        return cls(date.today().year, date.today().month, date.today().day)

    def __eq__(self, other):
        return (self.year, self.month, self.day) == (other.year, other.month, other.day)

def test_some_money_is_equal():
    # Create instances of SomeMoney for testing
    money1 = SomeMoney(FakeCurrency('USD'), Decimal('10.00'), FakeDate.today())
    money2 = SomeMoney(FakeCurrency('USD'), Decimal('10.00'), FakeDate.today())
    money3 = SomeMoney(FakeCurrency('EUR'), Decimal('10.00'), FakeDate.today())
    money4 = SomeMoney(FakeCurrency('USD'), Decimal('20.00'), FakeDate.today())
    money5 = SomeMoney(FakeCurrency('USD'), Decimal('10.00'), FakeDate(2023, 1, 1))
    not_money = (FakeCurrency('USD'), Decimal('10.00'), FakeDate.today())

    # Test is_equal method
    assert money1.is_equal(money2) == True, "money1 should be equal to money2"
    assert money1.is_equal(money3) == False, "money1 should not be equal to money3 with different currency"
    assert money1.is_equal(money4) == False, "money1 should not be equal to money4 with different quantity"
    assert money1.is_equal(money5) == False, "money1 should not be equal to money5 with different date of value"
    assert money1.is_equal(not_money) == False, "money1 should not be equal to a non-SomeMoney tuple"
