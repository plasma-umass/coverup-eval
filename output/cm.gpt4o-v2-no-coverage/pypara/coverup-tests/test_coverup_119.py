# file: pypara/monetary.py:421-422
# asked: {"lines": [421, 422], "branches": []}
# gained: {"lines": [421, 422], "branches": []}

import pytest
from decimal import Decimal
from pypara.monetary import SomeMoney
from pypara.currencies import Currency, CurrencyType
from pypara.commons.zeitgeist import Date

def test_some_money_is_equal():
    currency = Currency.of('USD', 'US Dollars', 2, CurrencyType.MONEY)
    date = Date(2023, 10, 1)
    money1 = SomeMoney(ccy=currency, qty=Decimal('100.00'), dov=date)
    money2 = SomeMoney(ccy=currency, qty=Decimal('100.00'), dov=date)
    money3 = SomeMoney(ccy=currency, qty=Decimal('200.00'), dov=date)
    
    assert money1.is_equal(money2) is True
    assert money1.is_equal(money3) is False
    assert money1.is_equal("not a SomeMoney instance") is False
