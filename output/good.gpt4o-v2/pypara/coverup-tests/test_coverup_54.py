# file: pypara/monetary.py:1278-1281
# asked: {"lines": [1278, 1279, 1280, 1281], "branches": []}
# gained: {"lines": [1278, 1279, 1280, 1281], "branches": []}

import pytest
from decimal import Decimal
from datetime import date as Date
from pypara.currencies import Currency, CurrencyType
from pypara.monetary import SomePrice, SomeMoney

def test_someprice_money():
    # Setup
    ccy = Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)
    qty = Decimal("100.00")
    dov = Date.today()
    some_price = SomePrice(ccy, qty, dov)

    # Exercise
    result = some_price.money

    # Verify
    assert isinstance(result, SomeMoney)
    assert result.ccy == ccy
    assert result.qty == qty.quantize(ccy.quantizer)
    assert result.dov == dov

    # Teardown
    # No teardown necessary as no external state is modified
