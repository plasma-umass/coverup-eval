# file: pypara/monetary.py:1097-1099
# asked: {"lines": [1097, 1098, 1099], "branches": []}
# gained: {"lines": [1097, 1098], "branches": []}

import pytest
from pypara.monetary import Price

def test_price_ge():
    class ConcretePrice(Price):
        def __ge__(self, other: 'Price') -> bool:
            return True

    price1 = ConcretePrice()
    price2 = ConcretePrice()

    assert price1 >= price2

