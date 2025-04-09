# file: pypara/monetary.py:552-553
# asked: {"lines": [552, 553], "branches": []}
# gained: {"lines": [552, 553], "branches": []}

import pytest
from decimal import Decimal
from pypara.monetary import SomeMoney
from pypara.currencies import Currency, CurrencyType
from datetime import date as Date

def test_with_dov():
    # Arrange
    currency = Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)
    quantity = Decimal("100.00")
    original_date = Date(2023, 1, 1)
    new_date = Date(2023, 12, 31)
    some_money = SomeMoney(currency, quantity, original_date)

    # Act
    updated_money = some_money.with_dov(new_date)

    # Assert
    assert updated_money.dov == new_date
    assert updated_money.ccy == some_money.ccy
    assert updated_money.qty == some_money.qty
    assert updated_money != some_money
