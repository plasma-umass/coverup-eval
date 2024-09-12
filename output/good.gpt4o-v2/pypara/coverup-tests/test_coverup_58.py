# file: pypara/monetary.py:524-529
# asked: {"lines": [524, 525, 526, 527, 528, 529], "branches": [[525, 526], [525, 527], [527, 528], [527, 529]]}
# gained: {"lines": [524], "branches": []}

import pytest
from decimal import Decimal
from datetime import date as Date
from typing import NamedTuple
from pypara.currencies import Currency, CurrencyType
from pypara.monetary import Money, IncompatibleCurrencyError

class SomeMoney(Money, NamedTuple("SomeMoney", [("ccy", Currency), ("qty", Decimal), ("dov", Date)])):
    defined = True
    undefined = False

    def lte(self, other: "Money") -> bool:
        if other.undefined:
            return False
        elif self.ccy != other.ccy:
            raise IncompatibleCurrencyError(ccy1=self.ccy, ccy2=other.ccy, operation="<= comparision")
        return self.qty <= other.qty

@pytest.fixture
def usd_currency():
    return Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)

@pytest.fixture
def eur_currency():
    return Currency.of("EUR", "Euro", 2, CurrencyType.MONEY)

@pytest.fixture
def some_money_usd(usd_currency):
    return SomeMoney(ccy=usd_currency, qty=Decimal("100.00"), dov=Date.today())

@pytest.fixture
def some_money_eur(eur_currency):
    return SomeMoney(ccy=eur_currency, qty=Decimal("100.00"), dov=Date.today())

@pytest.fixture
def undefined_money(usd_currency):
    class UndefinedMoney(Money):
        @property
        def undefined(self):
            return True

        @property
        def defined(self):
            return False

        def lte(self, other: "Money") -> bool:
            return False

    return UndefinedMoney()

def test_lte_with_undefined_money(some_money_usd, undefined_money):
    assert not some_money_usd.lte(undefined_money)

def test_lte_with_incompatible_currency(some_money_usd, some_money_eur):
    with pytest.raises(IncompatibleCurrencyError):
        some_money_usd.lte(some_money_eur)

def test_lte_with_compatible_currency(some_money_usd):
    other_money = SomeMoney(ccy=some_money_usd.ccy, qty=Decimal("200.00"), dov=Date.today())
    assert some_money_usd.lte(other_money)
