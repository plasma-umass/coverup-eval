# file: pypara/monetary.py:1375-1376
# asked: {"lines": [1375, 1376], "branches": []}
# gained: {"lines": [1375, 1376], "branches": []}

import pytest
from pypara.monetary import NonePrice, Price

class TestNonePrice:
    def test_lte_with_noneprice(self):
        none_price = NonePrice()
        other_price = NonePrice()
        assert none_price.lte(other_price) is True

    def test_lte_with_other_price(self, mocker):
        none_price = NonePrice()
        other_price = mocker.Mock(spec=Price)
        assert none_price.lte(other_price) is True
