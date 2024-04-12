# file pypara/monetary.py:433-435
# lines [433, 434, 435]
# branches []

import pytest
from decimal import Decimal
from pypara.monetary import SomeMoney, Currency, Date

@pytest.fixture
def currency_and_date():
    # Setup
    ccy = Currency('USD', 'US Dollar', 2, 'fiat', lambda x: x, True)
    dov = Date(2023, 1, 1)
    yield ccy, dov
    # Teardown (none needed in this case)

def test_abs_method_positive(currency_and_date):
    ccy, dov = currency_and_date
    qty = Decimal('100.00')
    money = SomeMoney(ccy, qty, dov)
    result = money.abs()
    assert result == SomeMoney(ccy, qty, dov), "abs() should return the same amount for positive quantities"

def test_abs_method_negative(currency_and_date):
    ccy, dov = currency_and_date
    qty = Decimal('-100.00')
    money = SomeMoney(ccy, qty, dov)
    result = money.abs()
    assert result == SomeMoney(ccy, abs(qty), dov), "abs() should return the positive amount for negative quantities"
