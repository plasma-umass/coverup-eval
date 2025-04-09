# file pypara/monetary.py:362-363
# lines [362, 363]
# branches []

import pytest
from pypara.monetary import Money

def test_money_rounding():
    # Create a mock Money object with a round method
    class MockMoney(Money):
        def round(self, ndigits):
            return f"Rounded to {ndigits} digits"

    money = MockMoney()

    # Test rounding with default ndigits
    result = round(money)
    assert result == "Rounded to 0 digits"

    # Test rounding with specific ndigits
    result = round(money, 2)
    assert result == "Rounded to 2 digits"

    # Test rounding with None as ndigits
    result = round(money, None)
    assert result == "Rounded to 0 digits"
