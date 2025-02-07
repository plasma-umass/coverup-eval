# file: pypara/monetary.py:994-1003
# asked: {"lines": [1003], "branches": []}
# gained: {"lines": [1003], "branches": []}

import pytest
from abc import ABC
from pypara.monetary import Price
from pypara.currencies import Currency, CurrencyType
from pypara.commons.zeitgeist import Date
from typing import Optional
from decimal import Decimal

def test_price_convert_not_implemented():
    class TestPrice(Price, ABC):
        def convert(self, to: Currency, asof: Optional[Date] = None, strict: bool = False) -> "Price":
            return super().convert(to, asof, strict)
    
    test_price = TestPrice()
    usd_currency = Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)
    with pytest.raises(NotImplementedError):
        test_price.convert(usd_currency)
