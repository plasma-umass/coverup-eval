# file: pypara/monetary.py:424-425
# asked: {"lines": [424, 425], "branches": []}
# gained: {"lines": [424, 425], "branches": []}

import pytest
from decimal import Decimal
from datetime import date as Date
from pypara.currencies import Currency, CurrencyType
from pypara.monetary import SomeMoney

class TestSomeMoney:
    def test_as_boolean(self):
        # Create a mock Currency
        currency = Currency.of("USD", "US Dollar", 2, CurrencyType.MONEY)
        
        # Test with a non-zero quantity
        money = SomeMoney(currency, Decimal('10.00'), Date.today())
        assert money.as_boolean() is True
        
        # Test with a zero quantity
        money = SomeMoney(currency, Decimal('0.00'), Date.today())
        assert money.as_boolean() is False
