# file: pypara/monetary.py:1182-1185
# asked: {"lines": [1182, 1184, 1185], "branches": []}
# gained: {"lines": [1182, 1184, 1185], "branches": []}

import pytest
from decimal import Decimal
from pypara.monetary import SomePrice
from pypara.currencies import Currency, CurrencyType
from datetime import date as Date

@pytest.fixture
def sample_data():
    ccy = Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)
    qty = Decimal("100.00")
    dov = Date.today()
    return SomePrice(ccy, qty, dov)

def test_scalar_subtract_with_int(sample_data):
    result = sample_data.scalar_subtract(10)
    assert result.qty == Decimal("90.00")
    assert result.ccy == sample_data.ccy
    assert result.dov == sample_data.dov

def test_scalar_subtract_with_float(sample_data):
    result = sample_data.scalar_subtract(10.5)
    assert result.qty == Decimal("89.50")
    assert result.ccy == sample_data.ccy
    assert result.dov == sample_data.dov

def test_scalar_subtract_with_decimal(sample_data):
    result = sample_data.scalar_subtract(Decimal("10.5"))
    assert result.qty == Decimal("89.50")
    assert result.ccy == sample_data.ccy
    assert result.dov == sample_data.dov

def test_scalar_subtract_with_amount(sample_data):
    amount = Decimal("10.5")  # Assuming Amount is a class that wraps Decimal
    result = sample_data.scalar_subtract(amount)
    assert result.qty == Decimal("89.50")
    assert result.ccy == sample_data.ccy
    assert result.dov == sample_data.dov

def test_scalar_subtract_with_quantity(sample_data):
    quantity = Decimal("10.5")  # Assuming Quantity is a class that wraps Decimal
    result = sample_data.scalar_subtract(quantity)
    assert result.qty == Decimal("89.50")
    assert result.ccy == sample_data.ccy
    assert result.dov == sample_data.dov
