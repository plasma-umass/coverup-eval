# file: pypara/monetary.py:545-546
# asked: {"lines": [545, 546], "branches": []}
# gained: {"lines": [545, 546], "branches": []}

import pytest
from decimal import Decimal
from datetime import date as Date
from pypara.monetary import Money, Currency, SomeMoney

@pytest.fixture
def currency_usd():
    return Currency(code="USD", name="US Dollar", decimals=2, type="fiat", quantizer=Decimal("0.01"), hashcache=None)

@pytest.fixture
def currency_eur():
    return Currency(code="EUR", name="Euro", decimals=2, type="fiat", quantizer=Decimal("0.01"), hashcache=None)

def test_somemoney_with_ccy(currency_usd, currency_eur):
    qty = Decimal("100.00")
    dov = Date(2023, 10, 1)
    
    some_money = SomeMoney(currency_usd, qty, dov)
    new_money = some_money.with_ccy(currency_eur)
    
    assert new_money.ccy == currency_eur
    assert new_money.qty == qty
    assert new_money.dov == dov
    assert isinstance(new_money, SomeMoney)
