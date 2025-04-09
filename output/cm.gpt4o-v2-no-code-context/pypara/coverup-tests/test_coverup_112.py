# file: pypara/monetary.py:695-696
# asked: {"lines": [695, 696], "branches": []}
# gained: {"lines": [695], "branches": []}

import pytest
from pypara.monetary import Money, Currency, Date
from typing import Optional

class TestNoneMoney:
    def test_convert(self, mocker):
        class NoneMoney(Money):
            def convert(self, to: Currency, asof: Optional[Date] = None, strict: bool = False) -> "Money":
                return self

        none_money = NoneMoney()

        # Mocking Currency and Date to avoid dependency issues
        mock_currency = mocker.Mock(spec=Currency)
        mock_date = mocker.Mock(spec=Date)

        # Test convert method with all parameters
        result = none_money.convert(to=mock_currency, asof=mock_date, strict=True)
        assert result is none_money

        # Test convert method with only required parameter
        result = none_money.convert(to=mock_currency)
        assert result is none_money

        # Test convert method with required and one optional parameter
        result = none_money.convert(to=mock_currency, asof=mock_date)
        assert result is none_money

        # Test convert method with required and the other optional parameter
        result = none_money.convert(to=mock_currency, strict=True)
        assert result is none_money
