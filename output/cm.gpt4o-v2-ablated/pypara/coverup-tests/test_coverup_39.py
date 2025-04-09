# file: pypara/monetary.py:1327-1328
# asked: {"lines": [1327, 1328], "branches": []}
# gained: {"lines": [1327, 1328], "branches": []}

import pytest
from pypara.monetary import NonePrice, Price

def test_noneprice_is_equal_with_noneprice():
    none_price1 = NonePrice()
    none_price2 = NonePrice()
    assert none_price1.is_equal(none_price2) == True

def test_noneprice_is_equal_with_other_price():
    none_price = NonePrice()
    other_price = Price()
    assert none_price.is_equal(other_price) == False

def test_noneprice_is_equal_with_non_price():
    none_price = NonePrice()
    non_price = "not a price"
    assert none_price.is_equal(non_price) == False
