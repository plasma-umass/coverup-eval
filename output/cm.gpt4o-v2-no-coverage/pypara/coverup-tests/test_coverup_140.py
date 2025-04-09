# file: pypara/monetary.py:695-696
# asked: {"lines": [695, 696], "branches": []}
# gained: {"lines": [695, 696], "branches": []}

import pytest
from pypara.monetary import NoneMoney
from pypara.currencies import Currency, CurrencyType
from pypara.commons.zeitgeist import Date

class TestNoneMoney:
    def test_convert(self):
        # Arrange
        none_money = NoneMoney()
        currency = Currency.of("USD", "US Dollar", 2, CurrencyType.MONEY)
        date = Date.today()

        # Act
        result = none_money.convert(currency, date, strict=True)

        # Assert
        assert result is none_money

        # Clean up
        del none_money
        del currency
        del date
        del result
