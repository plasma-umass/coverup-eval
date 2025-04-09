# file: pypara/monetary.py:1390-1391
# asked: {"lines": [1391], "branches": []}
# gained: {"lines": [1391], "branches": []}

import pytest
from pypara.monetary import NonePrice, Price
from datetime import date as Date

class TestNonePrice:
    def test_with_dov(self):
        none_price = NonePrice()
        dov = Date(2023, 10, 1)
        result = none_price.with_dov(dov)
        
        assert result is none_price
