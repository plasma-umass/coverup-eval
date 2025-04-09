# file: pypara/monetary.py:1159-1162
# asked: {"lines": [1159, 1161, 1162], "branches": []}
# gained: {"lines": [1159, 1161, 1162], "branches": []}

import pytest
from decimal import Decimal
from pypara.monetary import SomePrice
from pypara.currencies import Currency, CurrencyType
from pypara.commons.zeitgeist import Date

@pytest.fixture
def sample_price():
    ccy = Currency.of("USD", "US Dollar", 2, CurrencyType.MONEY)
    qty = Decimal("100.00")
    dov = Date(2023, 1, 1)
    return SomePrice(ccy, qty, dov)

def test_scalar_add_with_int(sample_price):
    result = sample_price.scalar_add(10)
    assert result.qty == Decimal("110.00")
    assert result.ccy == sample_price.ccy
    assert result.dov == sample_price.dov

def test_scalar_add_with_float(sample_price):
    result = sample_price.scalar_add(10.5)
    assert result.qty == Decimal("110.50")
    assert result.ccy == sample_price.ccy
    assert result.dov == sample_price.dov

def test_scalar_add_with_decimal(sample_price):
    result = sample_price.scalar_add(Decimal("10.5"))
    assert result.qty == Decimal("110.50")
    assert result.ccy == sample_price.ccy
    assert result.dov == sample_price.dov

def test_scalar_add_with_string(sample_price):
    result = sample_price.scalar_add("10.5")
    assert result.qty == Decimal("110.50")
    assert result.ccy == sample_price.ccy
    assert result.dov == sample_price.dov
