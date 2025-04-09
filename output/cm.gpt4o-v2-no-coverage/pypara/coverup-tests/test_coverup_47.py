# file: pypara/monetary.py:531-536
# asked: {"lines": [531, 532, 533, 534, 535, 536], "branches": [[532, 533], [532, 534], [534, 535], [534, 536]]}
# gained: {"lines": [531, 532, 533, 534, 535, 536], "branches": [[532, 533], [532, 534], [534, 535], [534, 536]]}

import pytest
from decimal import Decimal
from datetime import date as Date
from pypara.currencies import Currency, CurrencyType
from pypara.monetary import SomeMoney, IncompatibleCurrencyError

class MockMoney:
    def __init__(self, ccy, qty, undefined=False):
        self.ccy = ccy
        self.qty = qty
        self.undefined = undefined

@pytest.fixture
def usd():
    return Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)

@pytest.fixture
def eur():
    return Currency.of("EUR", "Euro", 2, CurrencyType.MONEY)

def test_some_money_gt_with_undefined_other(usd):
    some_money = SomeMoney(ccy=usd, qty=Decimal("100.00"), dov=Date.today())
    other_money = MockMoney(ccy=usd, qty=Decimal("50.00"), undefined=True)
    
    assert some_money.gt(other_money) is True

def test_some_money_gt_with_incompatible_currency(usd, eur):
    some_money = SomeMoney(ccy=usd, qty=Decimal("100.00"), dov=Date.today())
    other_money = MockMoney(ccy=eur, qty=Decimal("50.00"))
    
    with pytest.raises(IncompatibleCurrencyError) as excinfo:
        some_money.gt(other_money)
    
    assert excinfo.value.ccy1 == usd
    assert excinfo.value.ccy2 == eur
    assert excinfo.value.operation == "> comparision"

def test_some_money_gt_with_compatible_currency(usd):
    some_money = SomeMoney(ccy=usd, qty=Decimal("100.00"), dov=Date.today())
    other_money = MockMoney(ccy=usd, qty=Decimal("50.00"))
    
    assert some_money.gt(other_money) is True

    other_money.qty = Decimal("150.00")
    assert some_money.gt(other_money) is False
