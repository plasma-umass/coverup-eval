# file: pypara/monetary.py:1192-1194
# asked: {"lines": [1192, 1193, 1194], "branches": []}
# gained: {"lines": [1192, 1193, 1194], "branches": []}

import pytest
from decimal import Decimal
from pypara.monetary import SomePrice, SomeMoney
from pypara.currencies import Currency, CurrencyType
from pypara.commons.zeitgeist import Date

def test_someprice_times():
    # Setup
    ccy = Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)
    qty = Decimal("100.00")
    dov = Date.today()
    some_price = SomePrice(ccy, qty, dov)
    
    # Test
    result = some_price.times(2)
    
    # Assertions
    assert isinstance(result, SomeMoney)
    assert result.ccy == ccy
    assert result.qty == Decimal("200.00").quantize(ccy.quantizer)
    assert result.dov == dov
