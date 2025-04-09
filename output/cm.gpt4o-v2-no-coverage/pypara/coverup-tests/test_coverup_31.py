# file: pypara/monetary.py:538-543
# asked: {"lines": [538, 539, 540, 541, 542, 543], "branches": [[539, 540], [539, 541], [541, 542], [541, 543]]}
# gained: {"lines": [538, 539, 540, 541, 542, 543], "branches": [[539, 540], [539, 541], [541, 542], [541, 543]]}

import pytest
from decimal import Decimal
from pypara.monetary import SomeMoney, Money, IncompatibleCurrencyError
from pypara.currencies import Currency, CurrencyType
from pypara.commons.zeitgeist import Date

class MockMoney(Money):
    def __init__(self, ccy, qty, undefined=False):
        self.ccy = ccy
        self.qty = qty
        self.undefined = undefined

def test_gte_with_undefined_other():
    ccy = Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)
    qty = Decimal("100.00")
    dov = Date(2023, 1, 1)
    some_money = SomeMoney(ccy, qty, dov)
    other_money = MockMoney(ccy, qty, undefined=True)
    
    assert some_money.gte(other_money) is True

def test_gte_with_incompatible_currency():
    ccy1 = Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)
    ccy2 = Currency.of("EUR", "Euro", 2, CurrencyType.MONEY)
    qty = Decimal("100.00")
    dov = Date(2023, 1, 1)
    some_money = SomeMoney(ccy1, qty, dov)
    other_money = MockMoney(ccy2, qty)
    
    with pytest.raises(IncompatibleCurrencyError):
        some_money.gte(other_money)

def test_gte_with_compatible_currency():
    ccy = Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)
    qty1 = Decimal("100.00")
    qty2 = Decimal("50.00")
    dov = Date(2023, 1, 1)
    some_money = SomeMoney(ccy, qty1, dov)
    other_money = MockMoney(ccy, qty2)
    
    assert some_money.gte(other_money) is True

def test_gte_with_equal_currency_and_qty():
    ccy = Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)
    qty = Decimal("100.00")
    dov = Date(2023, 1, 1)
    some_money = SomeMoney(ccy, qty, dov)
    other_money = MockMoney(ccy, qty)
    
    assert some_money.gte(other_money) is True

def test_gte_with_lesser_qty():
    ccy = Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)
    qty1 = Decimal("50.00")
    qty2 = Decimal("100.00")
    dov = Date(2023, 1, 1)
    some_money = SomeMoney(ccy, qty1, dov)
    other_money = MockMoney(ccy, qty2)
    
    assert some_money.gte(other_money) is False
