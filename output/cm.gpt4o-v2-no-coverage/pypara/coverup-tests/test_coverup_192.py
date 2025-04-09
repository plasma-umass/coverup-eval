# file: pypara/monetary.py:1226-1231
# asked: {"lines": [1227, 1228, 1229, 1230, 1231], "branches": [[1227, 1228], [1227, 1229], [1229, 1230], [1229, 1231]]}
# gained: {"lines": [1227, 1228, 1229, 1230, 1231], "branches": [[1227, 1228], [1227, 1229], [1229, 1230], [1229, 1231]]}

import pytest
from decimal import Decimal
from datetime import date as Date
from pypara.monetary import SomePrice, IncompatibleCurrencyError
from pypara.currencies import Currency, CurrencyType

class MockPrice:
    def __init__(self, ccy, qty, undefined=False):
        self.ccy = ccy
        self.qty = qty
        self.undefined = undefined

def test_someprice_gt_with_undefined_other():
    ccy = Currency.of("USD", "US Dollar", 2, CurrencyType.MONEY)
    price1 = SomePrice(ccy=ccy, qty=Decimal("100.00"), dov=Date.today())
    other = MockPrice(ccy=ccy, qty=Decimal("50.00"), undefined=True)
    assert price1.gt(other) is True

def test_someprice_gt_with_incompatible_currency():
    ccy1 = Currency.of("USD", "US Dollar", 2, CurrencyType.MONEY)
    ccy2 = Currency.of("EUR", "Euro", 2, CurrencyType.MONEY)
    price1 = SomePrice(ccy=ccy1, qty=Decimal("100.00"), dov=Date.today())
    other = MockPrice(ccy=ccy2, qty=Decimal("50.00"))
    with pytest.raises(IncompatibleCurrencyError):
        price1.gt(other)

def test_someprice_gt_with_compatible_currency():
    ccy = Currency.of("USD", "US Dollar", 2, CurrencyType.MONEY)
    price1 = SomePrice(ccy=ccy, qty=Decimal("100.00"), dov=Date.today())
    other = MockPrice(ccy=ccy, qty=Decimal("50.00"))
    assert price1.gt(other) is True

def test_someprice_gt_with_equal_qty():
    ccy = Currency.of("USD", "US Dollar", 2, CurrencyType.MONEY)
    price1 = SomePrice(ccy=ccy, qty=Decimal("100.00"), dov=Date.today())
    other = MockPrice(ccy=ccy, qty=Decimal("100.00"))
    assert price1.gt(other) is False

def test_someprice_gt_with_lesser_qty():
    ccy = Currency.of("USD", "US Dollar", 2, CurrencyType.MONEY)
    price1 = SomePrice(ccy=ccy, qty=Decimal("50.00"), dov=Date.today())
    other = MockPrice(ccy=ccy, qty=Decimal("100.00"))
    assert price1.gt(other) is False
