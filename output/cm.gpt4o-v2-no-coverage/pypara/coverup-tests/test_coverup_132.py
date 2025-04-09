# file: pypara/monetary.py:686-687
# asked: {"lines": [686, 687], "branches": []}
# gained: {"lines": [686, 687], "branches": []}

import pytest
from pypara.monetary import NoneMoney
from pypara.currencies import Currency, CurrencyType
from decimal import Decimal

def test_none_money_with_ccy():
    none_money = NoneMoney()
    currency = Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)
    
    result = none_money.with_ccy(currency)
    
    assert result is none_money
