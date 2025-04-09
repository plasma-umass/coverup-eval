# file: pypara/monetary.py:1360-1361
# asked: {"lines": [1360, 1361], "branches": []}
# gained: {"lines": [1360, 1361], "branches": []}

import pytest
from decimal import Decimal
from pypara.monetary import NonePrice
from pypara.currencies import Currency
from pypara.commons.zeitgeist import Date

class MockPrice:
    def multiply(self, other):
        return self

def test_none_price_multiply():
    none_price = NonePrice()
    result = none_price.multiply(10)
    assert result is none_price

    result = none_price.multiply(Decimal('10.5'))
    assert result is none_price

    result = none_price.multiply(MockPrice())
    assert result is none_price
