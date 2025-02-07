# file: pypara/monetary.py:1137-1139
# asked: {"lines": [1137, 1138, 1139], "branches": []}
# gained: {"lines": [1137, 1138, 1139], "branches": []}

import pytest
from decimal import Decimal
from datetime import date as Date
from pypara.currencies import Currency, CurrencyType
from pypara.monetary import SomePrice

def test_someprice_round():
    # Setup
    currency = Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)
    quantity = Decimal("123.456")
    dov = Date(2023, 1, 1)
    price = SomePrice(currency, quantity, dov)

    # Execute
    rounded_price = price.round(2)

    # Verify
    assert rounded_price.ccy == currency
    assert rounded_price.qty == quantity.__round__(2)
    assert rounded_price.dov == dov

    # Cleanup - not necessary as no external state is modified

def test_someprice_round_default():
    # Setup
    currency = Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)
    quantity = Decimal("123.456")
    dov = Date(2023, 1, 1)
    price = SomePrice(currency, quantity, dov)

    # Execute
    rounded_price = price.round()

    # Verify
    assert rounded_price.ccy == currency
    assert rounded_price.qty == quantity.__round__(0)
    assert rounded_price.dov == dov

    # Cleanup - not necessary as no external state is modified
