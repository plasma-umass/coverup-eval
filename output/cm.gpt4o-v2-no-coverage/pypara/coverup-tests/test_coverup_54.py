# file: pypara/monetary.py:1212-1217
# asked: {"lines": [1212, 1213, 1214, 1215, 1216, 1217], "branches": [[1213, 1214], [1213, 1215], [1215, 1216], [1215, 1217]]}
# gained: {"lines": [1212, 1213, 1214, 1215, 1216, 1217], "branches": [[1213, 1214], [1213, 1215], [1215, 1216], [1215, 1217]]}

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

def test_lt_with_undefined_other():
    usd = Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)
    price1 = SomePrice(ccy=usd, qty=Decimal("10.00"), dov=Date.today())
    other = MockPrice(ccy=usd, qty=Decimal("20.00"), undefined=True)
    assert not price1.lt(other)

def test_lt_with_incompatible_currency():
    usd = Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)
    eur = Currency.of("EUR", "Euro", 2, CurrencyType.MONEY)
    price1 = SomePrice(ccy=usd, qty=Decimal("10.00"), dov=Date.today())
    other = MockPrice(ccy=eur, qty=Decimal("20.00"))
    with pytest.raises(IncompatibleCurrencyError):
        price1.lt(other)

def test_lt_with_compatible_currency():
    usd = Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)
    price1 = SomePrice(ccy=usd, qty=Decimal("10.00"), dov=Date.today())
    other = MockPrice(ccy=usd, qty=Decimal("20.00"))
    assert price1.lt(other)
