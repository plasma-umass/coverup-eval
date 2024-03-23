# file pypara/monetary.py:1219-1224
# lines [1220, 1221, 1222, 1223, 1224]
# branches ['1220->1221', '1220->1222', '1222->1223', '1222->1224']

import pytest
from decimal import Decimal
from pypara.monetary import SomePrice, Price, Currency, IncompatibleCurrencyError
from datetime import date

@pytest.fixture
def currency_mock(mocker):
    currency = mocker.Mock(spec=Currency)
    currency.code = 'USD'
    return currency

@pytest.fixture
def some_price(currency_mock):
    return SomePrice(currency_mock, Decimal('100.00'), date.today())

@pytest.fixture
def other_price_same_ccy(currency_mock):
    return SomePrice(currency_mock, Decimal('150.00'), date.today())

@pytest.fixture
def other_price_different_ccy(mocker):
    different_currency_mock = mocker.Mock(spec=Currency)
    different_currency_mock.code = 'EUR'
    return SomePrice(different_currency_mock, Decimal('100.00'), date.today())

@pytest.fixture
def other_price_undefined():
    class UndefinedPrice(Price):
        @property
        def undefined(self):
            return True

    return UndefinedPrice()

def test_lte_with_undefined_other(some_price, other_price_undefined):
    assert not some_price.lte(other_price_undefined)

def test_lte_with_different_currency(some_price, other_price_different_ccy):
    with pytest.raises(IncompatibleCurrencyError) as exc_info:
        some_price.lte(other_price_different_ccy)
    assert exc_info.value.ccy1.code == some_price.ccy.code
    assert exc_info.value.ccy2.code == other_price_different_ccy.ccy.code
    assert '<= comparision' in str(exc_info.value)

def test_lte_with_same_currency(some_price, other_price_same_ccy):
    assert some_price.lte(other_price_same_ccy)
