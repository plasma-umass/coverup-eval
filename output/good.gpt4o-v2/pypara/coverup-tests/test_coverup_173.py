# file: pypara/monetary.py:1113-1114
# asked: {"lines": [1113, 1114], "branches": []}
# gained: {"lines": [1113, 1114], "branches": []}

import pytest
from decimal import Decimal
from datetime import date as Date
from pypara.currencies import Currency, CurrencyType
from pypara.monetary import SomePrice

def test_someprice_is_equal():
    ccy = Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)
    qty = Decimal("100.00")
    dov = Date(2023, 1, 1)
    
    price1 = SomePrice(ccy, qty, dov)
    price2 = SomePrice(ccy, qty, dov)
    price3 = SomePrice(ccy, Decimal("200.00"), dov)
    
    assert price1.is_equal(price2) is True
    assert price1.is_equal(price3) is False
    assert price1.is_equal("not a price") is False
