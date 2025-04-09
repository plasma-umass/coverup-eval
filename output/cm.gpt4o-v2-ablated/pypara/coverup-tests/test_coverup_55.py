# file: pypara/monetary.py:531-536
# asked: {"lines": [532, 533, 534, 535, 536], "branches": [[532, 533], [532, 534], [534, 535], [534, 536]]}
# gained: {"lines": [532, 533, 534, 535, 536], "branches": [[532, 533], [532, 534], [534, 535], [534, 536]]}

import pytest
from decimal import Decimal
from datetime import date as Date
from pypara.monetary import SomeMoney, Money, Currency, IncompatibleCurrencyError

class MockCurrency:
    def __init__(self, code):
        self.code = code

class MockMoney:
    def __init__(self, ccy, qty, undefined=False):
        self.ccy = ccy
        self.qty = qty
        self.undefined = undefined

def test_gt_with_undefined_other():
    ccy = MockCurrency("USD")
    some_money = SomeMoney(ccy=ccy, qty=Decimal("100.00"), dov=Date.today())
    other_money = MockMoney(ccy=ccy, qty=Decimal("50.00"), undefined=True)
    assert some_money.gt(other_money) is True

def test_gt_with_incompatible_currency():
    ccy1 = MockCurrency("USD")
    ccy2 = MockCurrency("EUR")
    some_money = SomeMoney(ccy=ccy1, qty=Decimal("100.00"), dov=Date.today())
    other_money = MockMoney(ccy=ccy2, qty=Decimal("50.00"))
    with pytest.raises(IncompatibleCurrencyError):
        some_money.gt(other_money)

def test_gt_with_compatible_currency():
    ccy = MockCurrency("USD")
    some_money = SomeMoney(ccy=ccy, qty=Decimal("100.00"), dov=Date.today())
    other_money = MockMoney(ccy=ccy, qty=Decimal("50.00"))
    assert some_money.gt(other_money) is True

def test_gt_with_equal_currency_and_qty():
    ccy = MockCurrency("USD")
    some_money = SomeMoney(ccy=ccy, qty=Decimal("100.00"), dov=Date.today())
    other_money = MockMoney(ccy=ccy, qty=Decimal("100.00"))
    assert some_money.gt(other_money) is False
