# file: pypara/monetary.py:445-448
# asked: {"lines": [445, 446, 447, 448], "branches": []}
# gained: {"lines": [445, 446, 447, 448], "branches": []}

import pytest
from decimal import Decimal
from pypara.monetary import SomeMoney
from pypara.currencies import Currency, CurrencyType
from pypara.commons.zeitgeist import Date

@pytest.fixture
def some_money():
    ccy = Currency.of('USD', 'US Dollar', 2, CurrencyType.MONEY)
    qty = Decimal('123.456')
    dov = Date(2023, 10, 1)  # Assuming Date takes year, month, day
    return SomeMoney(ccy, qty, dov)

def test_some_money_init(some_money):
    assert some_money.ccy.code == 'USD'
    assert some_money.ccy.decimals == 2
    assert some_money.qty == Decimal('123.456')
    assert some_money.dov.year == 2023
    assert some_money.dov.month == 10
    assert some_money.dov.day == 1

def test_some_money_round(some_money):
    rounded_money = some_money.round(1)
    assert rounded_money.qty == Decimal('123.5')
    assert rounded_money.ccy == some_money.ccy
    assert rounded_money.dov == some_money.dov

    rounded_money = some_money.round(2)
    assert rounded_money.qty == Decimal('123.46')
    assert rounded_money.ccy == some_money.ccy
    assert rounded_money.dov == some_money.dov

    rounded_money = some_money.round(0)
    assert rounded_money.qty == Decimal('123')
    assert rounded_money.ccy == some_money.ccy
    assert rounded_money.dov == some_money.dov
