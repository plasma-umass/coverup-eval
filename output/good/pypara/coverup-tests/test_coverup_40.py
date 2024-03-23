# file pypara/monetary.py:1233-1238
# lines [1233, 1234, 1235, 1236, 1237, 1238]
# branches ['1234->1235', '1234->1236', '1236->1237', '1236->1238']

import pytest
from decimal import Decimal
from datetime import date
from pypara.monetary import SomePrice, Price, Currency, IncompatibleCurrencyError

@pytest.fixture
def currency_mock(mocker):
    mock_currency = mocker.Mock(spec=Currency)
    mock_currency.code = 'USD'
    return mock_currency

@pytest.fixture
def different_currency_mock(mocker):
    mock_currency = mocker.Mock(spec=Currency)
    mock_currency.code = 'EUR'
    return mock_currency

@pytest.fixture
def some_price(currency_mock):
    return SomePrice(currency_mock, Decimal('100.00'), date.today())

@pytest.fixture
def other_price_same_ccy(currency_mock):
    return SomePrice(currency_mock, Decimal('90.00'), date.today())

@pytest.fixture
def other_price_different_ccy(different_currency_mock):
    return SomePrice(different_currency_mock, Decimal('100.00'), date.today())

@pytest.fixture
def undefined_price(mocker):
    mock_price = mocker.Mock(spec=Price)
    mock_price.undefined = True
    return mock_price

def test_gte_with_undefined_other(some_price, undefined_price):
    assert some_price.gte(undefined_price) is True

def test_gte_with_same_currency(some_price, other_price_same_ccy):
    assert some_price.gte(other_price_same_ccy) is True

def test_gte_with_different_currency_raises_error(some_price, other_price_different_ccy):
    with pytest.raises(IncompatibleCurrencyError) as exc_info:
        some_price.gte(other_price_different_ccy)
    assert exc_info.value.ccy1.code == some_price.ccy.code
    assert exc_info.value.ccy2.code == other_price_different_ccy.ccy.code
    assert 'operation' in exc_info.value.args[0]
