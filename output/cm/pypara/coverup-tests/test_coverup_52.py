# file pypara/monetary.py:473-489
# lines [473, 474, 475, 483, 484, 486, 487, 489]
# branches ['474->475', '474->477', '486->487', '486->489']

import pytest
from decimal import Decimal
from datetime import date
from pypara.monetary import SomeMoney, Money, Currency, IncompatibleCurrencyError

@pytest.fixture
def currency_usd(mocker):
    mock_currency = mocker.Mock(spec=Currency)
    mock_currency.code = 'USD'
    return mock_currency

@pytest.fixture
def currency_eur(mocker):
    mock_currency = mocker.Mock(spec=Currency)
    mock_currency.code = 'EUR'
    return mock_currency

@pytest.fixture
def some_money(currency_usd):
    return SomeMoney(currency_usd, Decimal('100.00'), date(2021, 1, 1))

@pytest.fixture
def other_money(currency_usd):
    return SomeMoney(currency_usd, Decimal('50.00'), date(2021, 1, 2))

@pytest.fixture
def other_money_different_currency(currency_eur):
    return SomeMoney(currency_eur, Decimal('50.00'), date(2021, 1, 2))

@pytest.fixture
def undefined_money(mocker):
    mock_money = mocker.Mock(spec=Money)
    mock_money.undefined = True
    return mock_money

def test_subtract_same_currency(some_money, other_money):
    result = some_money.subtract(other_money)
    assert result.qty == Decimal('50.00')
    assert result.dov == date(2021, 1, 2)

def test_subtract_undefined_money(some_money, undefined_money):
    result = some_money.subtract(undefined_money)
    assert result == some_money

def test_subtract_different_currency_raises_error(some_money, other_money_different_currency):
    with pytest.raises(IncompatibleCurrencyError) as exc_info:
        some_money.subtract(other_money_different_currency)
    assert exc_info.value.operation == "subtraction"
