# file: pypara/monetary.py:517-522
# asked: {"lines": [518, 519, 520, 521, 522], "branches": [[518, 519], [518, 520], [520, 521], [520, 522]]}
# gained: {"lines": [518, 519, 520, 521, 522], "branches": [[518, 519], [518, 520], [520, 521], [520, 522]]}

import pytest
from decimal import Decimal
from datetime import date as Date
from pypara.monetary import SomeMoney, Money, Currency, IncompatibleCurrencyError

class MockCurrency:
    def __init__(self, code):
        self.code = code

class MockMoney(Money):
    def __init__(self, ccy, qty, undefined=False):
        self.ccy = ccy
        self.qty = qty
        self.undefined = undefined

@pytest.fixture
def currency_usd():
    return MockCurrency("USD")

@pytest.fixture
def currency_eur():
    return MockCurrency("EUR")

@pytest.fixture
def some_money_usd(currency_usd):
    return SomeMoney(ccy=currency_usd, qty=Decimal("100.00"), dov=Date.today())

@pytest.fixture
def some_money_usd_less(currency_usd):
    return SomeMoney(ccy=currency_usd, qty=Decimal("50.00"), dov=Date.today())

@pytest.fixture
def some_money_eur(currency_eur):
    return SomeMoney(ccy=currency_eur, qty=Decimal("100.00"), dov=Date.today())

@pytest.fixture
def undefined_money(currency_usd):
    return MockMoney(ccy=currency_usd, qty=Decimal("100.00"), undefined=True)

def test_lt_undefined_money(some_money_usd, undefined_money):
    assert not some_money_usd.lt(undefined_money)

def test_lt_incompatible_currency(some_money_usd, some_money_eur):
    with pytest.raises(IncompatibleCurrencyError):
        some_money_usd.lt(some_money_eur)

def test_lt_less_quantity(some_money_usd, some_money_usd_less):
    assert not some_money_usd.lt(some_money_usd_less)
    assert some_money_usd_less.lt(some_money_usd)

def test_lt_equal_quantity(some_money_usd):
    assert not some_money_usd.lt(some_money_usd)
