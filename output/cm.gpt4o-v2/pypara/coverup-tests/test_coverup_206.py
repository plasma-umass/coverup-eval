# file: pypara/monetary.py:1233-1238
# asked: {"lines": [1234, 1235, 1236, 1237, 1238], "branches": [[1234, 1235], [1234, 1236], [1236, 1237], [1236, 1238]]}
# gained: {"lines": [1234, 1235, 1236, 1237, 1238], "branches": [[1234, 1235], [1234, 1236], [1236, 1237], [1236, 1238]]}

import pytest
from decimal import Decimal
from datetime import date as Date
from pypara.currencies import Currency, CurrencyType
from pypara.monetary import SomePrice, IncompatibleCurrencyError

class MockPrice:
    def __init__(self, undefined, ccy, qty):
        self.undefined = undefined
        self.ccy = ccy
        self.qty = qty

def test_gte_with_undefined_other():
    price1 = SomePrice(ccy=Currency.of("USD", "US Dollar", 2, CurrencyType.MONEY), qty=Decimal("100.00"), dov=Date.today())
    other = MockPrice(undefined=True, ccy=Currency.of("USD", "US Dollar", 2, CurrencyType.MONEY), qty=Decimal("50.00"))
    assert price1.gte(other) is True

def test_gte_with_incompatible_currency():
    price1 = SomePrice(ccy=Currency.of("USD", "US Dollar", 2, CurrencyType.MONEY), qty=Decimal("100.00"), dov=Date.today())
    other = MockPrice(undefined=False, ccy=Currency.of("EUR", "Euro", 2, CurrencyType.MONEY), qty=Decimal("50.00"))
    with pytest.raises(IncompatibleCurrencyError):
        price1.gte(other)

def test_gte_with_compatible_currency():
    price1 = SomePrice(ccy=Currency.of("USD", "US Dollar", 2, CurrencyType.MONEY), qty=Decimal("100.00"), dov=Date.today())
    other = MockPrice(undefined=False, ccy=Currency.of("USD", "US Dollar", 2, CurrencyType.MONEY), qty=Decimal("50.00"))
    assert price1.gte(other) is True

def test_gte_with_equal_qty():
    price1 = SomePrice(ccy=Currency.of("USD", "US Dollar", 2, CurrencyType.MONEY), qty=Decimal("100.00"), dov=Date.today())
    other = MockPrice(undefined=False, ccy=Currency.of("USD", "US Dollar", 2, CurrencyType.MONEY), qty=Decimal("100.00"))
    assert price1.gte(other) is True

def test_gte_with_lesser_qty():
    price1 = SomePrice(ccy=Currency.of("USD", "US Dollar", 2, CurrencyType.MONEY), qty=Decimal("100.00"), dov=Date.today())
    other = MockPrice(undefined=False, ccy=Currency.of("USD", "US Dollar", 2, CurrencyType.MONEY), qty=Decimal("150.00"))
    assert price1.gte(other) is False
