# file: pypara/monetary.py:1390-1391
# asked: {"lines": [1390, 1391], "branches": []}
# gained: {"lines": [1390], "branches": []}

import pytest
from pypara.monetary import Price

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

class NonePrice(Price):
    def with_dov(self, dov: Date) -> "Price":
        return self

def test_noneprice_with_dov():
    none_price = NonePrice()
    dov = Date(2023, 10, 1)
    result = none_price.with_dov(dov)
    assert result is none_price
