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

def test_price_of_with_none_values(usd_currency):
    assert Price.of(None, None, None) is NoPrice
    assert Price.of(usd_currency, None, None) is NoPrice
    assert Price.of(None, Decimal('10.0'), None) is NoPrice
    assert Price.of(None, None, Date(2023, 1, 1)) is NoPrice
    assert Price.of(usd_currency, Decimal('10.0'), None) is NoPrice
    assert Price.of(usd_currency, None, Date(2023, 1, 1)) is NoPrice
    assert Price.of(None, Decimal('10.0'), Date(2023, 1, 1)) is NoPrice

def test_price_of_with_valid_values(usd_currency):
    qty = Decimal('10.0')
    dov = Date(2023, 1, 1)
    price = Price.of(usd_currency, qty, dov)
    assert isinstance(price, SomePrice)
    assert price.ccy == usd_currency
    assert price.qty == qty
    assert price.dov == dov
