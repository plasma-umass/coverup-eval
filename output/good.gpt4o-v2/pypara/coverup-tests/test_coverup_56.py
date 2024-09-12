# file: pypara/monetary.py:1226-1231
# asked: {"lines": [1226, 1227, 1228, 1229, 1230, 1231], "branches": [[1227, 1228], [1227, 1229], [1229, 1230], [1229, 1231]]}
# gained: {"lines": [1226, 1227, 1228, 1229, 1230, 1231], "branches": [[1227, 1228], [1227, 1229], [1229, 1230], [1229, 1231]]}

import pytest
from decimal import Decimal
from datetime import date as Date
from pypara.currencies import Currency, CurrencyType
from pypara.monetary import SomePrice, IncompatibleCurrencyError

class MockPrice:
    def __init__(self, ccy, qty, undefined=False):
        self.ccy = ccy
        self.qty = qty
        self.undefined = undefined

def test_someprice_gt_with_undefined_other():
    usd = Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)
    price1 = SomePrice(ccy=usd, qty=Decimal("100.00"), dov=Date.today())
    other = MockPrice(ccy=usd, qty=Decimal("50.00"), undefined=True)
    
    assert price1.gt(other) is True

def test_someprice_gt_with_incompatible_currency():
    usd = Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)
    eur = Currency.of("EUR", "Euro", 2, CurrencyType.MONEY)
    price1 = SomePrice(ccy=usd, qty=Decimal("100.00"), dov=Date.today())
    other = MockPrice(ccy=eur, qty=Decimal("50.00"))
    
    with pytest.raises(IncompatibleCurrencyError) as excinfo:
        price1.gt(other)
    
    assert excinfo.value.ccy1 == usd
    assert excinfo.value.ccy2 == eur
    assert excinfo.value.operation == "> comparision"

def test_someprice_gt_with_compatible_currency():
    usd = Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)
    price1 = SomePrice(ccy=usd, qty=Decimal("100.00"), dov=Date.today())
    other = MockPrice(ccy=usd, qty=Decimal("50.00"))
    
    assert price1.gt(other) is True

    other.qty = Decimal("150.00")
    assert price1.gt(other) is False
