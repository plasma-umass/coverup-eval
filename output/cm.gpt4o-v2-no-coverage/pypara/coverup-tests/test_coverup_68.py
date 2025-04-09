# file: pypara/monetary.py:302-311
# asked: {"lines": [302, 303, 311], "branches": []}
# gained: {"lines": [302, 303], "branches": []}

import pytest
from abc import ABC
from typing import Optional
from pypara.monetary import Money
from pypara.currencies import Currency, CurrencyType
from pypara.commons.zeitgeist import Date
from pypara.exchange import FXRateLookupError

class TestMoney(Money, ABC):
    def __init__(self, currency: Currency):
        self.currency = currency

    def convert(self, to: Currency, asof: Optional[Date] = None, strict: bool = False) -> "Money":
        if not isinstance(to, Currency):
            raise FXRateLookupError(self.currency, to, asof or Date.today())
        return self

def test_convert_success():
    usd = Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)
    money = TestMoney(usd)
    result = money.convert(usd)
    assert result is money

def test_convert_failure():
    usd = Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)
    money = TestMoney(usd)
    invalid_currency = "INVALID"
    with pytest.raises(FXRateLookupError):
        money.convert(invalid_currency)
