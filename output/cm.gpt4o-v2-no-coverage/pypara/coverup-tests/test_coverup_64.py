# file: pypara/monetary.py:584-586
# asked: {"lines": [584, 585, 586], "branches": []}
# gained: {"lines": [584, 585, 586], "branches": []}

import pytest
from decimal import Decimal
from pypara.monetary import SomeMoney, SomePrice
from pypara.currencies import Currency, CurrencyType
from pypara.commons.zeitgeist import Date

def test_some_money_price():
    ccy = Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)
    qty = Decimal("100.0")
    dov = Date(2023, 10, 1)
    some_money = SomeMoney(ccy, qty, dov)
    
    price = some_money.price
    
    assert isinstance(price, SomePrice)
    assert price.ccy == ccy
    assert price.qty == qty
    assert price.dov == dov
