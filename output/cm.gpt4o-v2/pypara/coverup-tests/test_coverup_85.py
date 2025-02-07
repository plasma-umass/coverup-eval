# file: pypara/monetary.py:584-586
# asked: {"lines": [584, 585, 586], "branches": []}
# gained: {"lines": [584, 585, 586], "branches": []}

import pytest
from decimal import Decimal
from datetime import date as Date
from pypara.currencies import Currency, CurrencyType
from pypara.monetary import SomeMoney, SomePrice

def test_some_money_price():
    # Create instances of Currency, Decimal, and Date
    currency = Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)
    quantity = Decimal("100.00")
    date_of_value = Date.today()

    # Create an instance of SomeMoney
    some_money = SomeMoney(ccy=currency, qty=quantity, dov=date_of_value)

    # Access the price property to trigger the code
    price = some_money.price

    # Assertions to verify the postconditions
    assert isinstance(price, SomePrice)
    assert price.ccy == currency
    assert price.qty == quantity
    assert price.dov == date_of_value
