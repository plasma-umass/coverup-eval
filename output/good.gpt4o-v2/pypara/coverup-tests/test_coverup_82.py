# file: pypara/monetary.py:496-499
# asked: {"lines": [496, 498, 499], "branches": []}
# gained: {"lines": [496, 498, 499], "branches": []}

import pytest
from decimal import Decimal
from pypara.monetary import SomeMoney
from pypara.currencies import Currency, CurrencyType
from datetime import date as Date

@pytest.fixture
def sample_currency():
    return Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)

@pytest.fixture
def sample_date():
    return Date.today()

@pytest.fixture
def sample_money(sample_currency, sample_date):
    return SomeMoney(sample_currency, Decimal("100.00"), sample_date)

def test_multiply_with_int(sample_money):
    result = sample_money.multiply(2)
    assert result.qty == Decimal("200.00")
    assert result.ccy == sample_money.ccy
    assert result.dov == sample_money.dov

def test_multiply_with_float(sample_money):
    result = sample_money.multiply(2.5)
    assert result.qty == Decimal("250.00")
    assert result.ccy == sample_money.ccy
    assert result.dov == sample_money.dov

def test_multiply_with_decimal(sample_money):
    result = sample_money.multiply(Decimal("1.5"))
    assert result.qty == Decimal("150.00")
    assert result.ccy == sample_money.ccy
    assert result.dov == sample_money.dov

def test_multiply_with_string(sample_money):
    result = sample_money.multiply("3")
    assert result.qty == Decimal("300.00")
    assert result.ccy == sample_money.ccy
    assert result.dov == sample_money.dov
