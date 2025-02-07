# file: pypara/monetary.py:1013-1020
# asked: {"lines": [1013, 1014, 1018, 1019, 1020], "branches": [[1018, 1019], [1018, 1020]]}
# gained: {"lines": [1013, 1014, 1018, 1019, 1020], "branches": [[1018, 1019], [1018, 1020]]}

import pytest
from decimal import Decimal
from pypara.commons.zeitgeist import Date
from pypara.currencies import Currency, CurrencyType
from pypara.monetary import Price, NoPrice, SomePrice

@pytest.fixture
def usd_currency():
    return Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)

@pytest.fixture
def sample_date():
    return Date(2023, 1, 1)

def test_price_of_with_none_values(usd_currency, sample_date):
    assert Price.of(None, None, None) is NoPrice
    assert Price.of(usd_currency, None, None) is NoPrice
    assert Price.of(None, Decimal('10.00'), None) is NoPrice
    assert Price.of(None, None, sample_date) is NoPrice
    assert Price.of(usd_currency, Decimal('10.00'), None) is NoPrice
    assert Price.of(usd_currency, None, sample_date) is NoPrice
    assert Price.of(None, Decimal('10.00'), sample_date) is NoPrice

def test_price_of_with_valid_values(usd_currency, sample_date):
    qty = Decimal('10.00')
    price = Price.of(usd_currency, qty, sample_date)
    assert isinstance(price, SomePrice)
    assert price.ccy == usd_currency
    assert price.qty == qty
    assert price.dov == sample_date
