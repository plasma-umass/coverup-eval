# file: pypara/monetary.py:445-448
# asked: {"lines": [446, 447, 448], "branches": []}
# gained: {"lines": [446, 447, 448], "branches": []}

import pytest
from decimal import Decimal
from pypara.monetary import SomeMoney
from pypara.currencies import Currency, CurrencyType
from pypara.commons.zeitgeist import Date

def test_some_money_round():
    # Setup
    currency = Currency.of("USD", "US Dollar", 2, CurrencyType.MONEY)
    quantity = Decimal("123.456")
    date_of_value = Date.today()
    some_money = SomeMoney(currency, quantity, date_of_value)

    # Test rounding with ndigits less than currency decimals
    rounded_money = some_money.round(1)
    assert rounded_money.qty == Decimal("123.5")
    assert rounded_money.ccy == currency
    assert rounded_money.dov == date_of_value

    # Test rounding with ndigits equal to currency decimals
    rounded_money = some_money.round(2)
    assert rounded_money.qty == Decimal("123.46")
    assert rounded_money.ccy == currency
    assert rounded_money.dov == date_of_value

    # Test rounding with ndigits greater than currency decimals
    rounded_money = some_money.round(3)
    assert rounded_money.qty == Decimal("123.46")
    assert rounded_money.ccy == currency
    assert rounded_money.dov == date_of_value
