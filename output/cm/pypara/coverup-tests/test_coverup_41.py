# file pypara/monetary.py:450-466
# lines [450, 451, 452, 460, 461, 463, 464, 466]
# branches ['451->452', '451->454', '463->464', '463->466']

import pytest
from decimal import Decimal
from datetime import date
from pypara.monetary import SomeMoney, Money, Currency, IncompatibleCurrencyError

class FakeCurrency:
    def __init__(self, code):
        self.code = code

    def __eq__(self, other):
        return self.code == other.code

@pytest.fixture
def usd_currency():
    return FakeCurrency('USD')

@pytest.fixture
def eur_currency():
    return FakeCurrency('EUR')

@pytest.fixture
def some_money(usd_currency):
    return SomeMoney(usd_currency, Decimal('100.00'), date(2021, 1, 1))

@pytest.fixture
def other_money(usd_currency):
    return SomeMoney(usd_currency, Decimal('50.00'), date(2021, 1, 2))

@pytest.fixture
def other_currency_money(eur_currency):
    return SomeMoney(eur_currency, Decimal('50.00'), date(2021, 1, 2))

def test_add_same_currency(some_money, other_money):
    result = some_money.add(other_money)
    assert result.qty == Decimal('150.00')
    assert result.dov == date(2021, 1, 2)

def test_add_different_currency(some_money, other_currency_money):
    with pytest.raises(IncompatibleCurrencyError) as exc_info:
        some_money.add(other_currency_money)
    assert exc_info.value.ccy1.code == 'USD'
    assert exc_info.value.ccy2.code == 'EUR'
    assert exc_info.value.operation == "addition"

def test_add_undefined_money(mocker, some_money):
    undefined_money = mocker.Mock(spec=Money)
    undefined_money.undefined = True
    result = some_money.add(undefined_money)
    assert result == some_money
