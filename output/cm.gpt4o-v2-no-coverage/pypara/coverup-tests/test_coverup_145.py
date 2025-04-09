# file: pypara/monetary.py:1113-1114
# asked: {"lines": [1113, 1114], "branches": []}
# gained: {"lines": [1113, 1114], "branches": []}

import pytest
from decimal import Decimal
from pypara.commons.zeitgeist import Date
from pypara.currencies import Currency, CurrencyType
from pypara.monetary import SomePrice

def test_someprice_is_equal():
    ccy = Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)
    qty = Decimal('100.0')
    dov = Date(2023, 10, 1)
    
    price1 = SomePrice(ccy, qty, dov)
    price2 = SomePrice(ccy, qty, dov)
    price3 = SomePrice(Currency.of("EUR", "Euro", 2, CurrencyType.MONEY), qty, dov)
    price4 = (ccy, qty, dov)  # Not an instance of SomePrice

    assert price1.is_equal(price2) is True
    assert price1.is_equal(price3) is False
    assert price1.is_equal(price4) is False
