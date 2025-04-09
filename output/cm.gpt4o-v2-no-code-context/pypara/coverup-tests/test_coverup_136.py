# file: pypara/monetary.py:421-422
# asked: {"lines": [422], "branches": []}
# gained: {"lines": [422], "branches": []}

import pytest
from decimal import Decimal
from datetime import date as Date
from pypara.monetary import SomeMoney, Currency

def test_some_money_is_equal():
    currency = Currency(code="USD", name="US Dollar", decimals=2, type="fiat", quantizer=Decimal("0.01"), hashcache=None)
    some_money1 = SomeMoney(ccy=currency, qty=Decimal("100.00"), dov=Date(2023, 1, 1))
    some_money2 = SomeMoney(ccy=currency, qty=Decimal("100.00"), dov=Date(2023, 1, 1))
    some_money3 = SomeMoney(ccy=currency, qty=Decimal("200.00"), dov=Date(2023, 1, 1))

    assert some_money1.is_equal(some_money2) is True
    assert some_money1.is_equal(some_money3) is False
    assert some_money1.is_equal("not a SomeMoney instance") is False
