# file: pypara/monetary.py:659-660
# asked: {"lines": [659, 660], "branches": []}
# gained: {"lines": [659, 660], "branches": []}

import pytest
from decimal import Decimal
from pypara.monetary import NoneMoney, Money
from pypara.currencies import Currency, CurrencyType
from pypara.commons.zeitgeist import Date

class TestNoneMoney:
    
    def test_subtract(self):
        # Create instances of Money and NoneMoney using the 'of' class method
        currency = Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)
        quantity = Decimal('100.00')
        date_of_value = Date.today()  # Assuming Date has a today() method
        
        money_instance = Money.of(currency, quantity, date_of_value)
        none_money_instance = NoneMoney()
        
        # Perform the subtraction
        result = none_money_instance.subtract(money_instance)
        
        # Assert that the result is the negation of money_instance
        assert result == -money_instance

        # Clean up if necessary (depends on the implementation details of Money and NoneMoney)
        del money_instance
        del none_money_instance
