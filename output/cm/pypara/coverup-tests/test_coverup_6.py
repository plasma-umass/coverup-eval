# file pypara/monetary.py:1013-1020
# lines [1013, 1014, 1018, 1019, 1020]
# branches ['1018->1019', '1018->1020']

import pytest
from decimal import Decimal
from datetime import date
from pypara.monetary import Price, NoPrice, SomePrice, Currency

@pytest.fixture
def currency_mock(mocker):
    return mocker.MagicMock(spec=Currency)

@pytest.fixture
def date_mock(mocker):
    return mocker.MagicMock(spec=date)

def test_price_of_with_none_values_returns_noprice(currency_mock, date_mock):
    assert Price.of(None, Decimal('10.00'), date_mock) is NoPrice
    assert Price.of(currency_mock, None, date_mock) is NoPrice
    assert Price.of(currency_mock, Decimal('10.00'), None) is NoPrice

def test_price_of_with_valid_values_returns_someprice(currency_mock, date_mock):
    qty = Decimal('10.00')
    dov = date_mock
    price = Price.of(currency_mock, qty, dov)
    assert isinstance(price, SomePrice)
    assert price.ccy == currency_mock
    assert price.qty == qty
    assert price.dov == dov
