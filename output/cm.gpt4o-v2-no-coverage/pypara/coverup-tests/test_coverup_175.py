# file: pypara/monetary.py:433-435
# asked: {"lines": [434, 435], "branches": []}
# gained: {"lines": [434, 435], "branches": []}

import pytest
from decimal import Decimal
from pypara.monetary import SomeMoney
from pypara.currencies import Currency, CurrencyType
from pypara.commons.zeitgeist import Date

def test_somemoney_abs():
    currency = Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)
    quantity = Decimal("-100.00")
    date_of_value = Date(2023, 10, 1)
    
    money_instance = SomeMoney(currency, quantity, date_of_value)
    abs_money_instance = money_instance.abs()
    
    assert abs_money_instance.qty == abs(quantity)
    assert abs_money_instance.ccy == currency
    assert abs_money_instance.dov == date_of_value
