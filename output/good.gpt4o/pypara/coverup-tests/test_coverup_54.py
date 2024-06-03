# file pypara/monetary.py:1057-1059
# lines [1057, 1058, 1059]
# branches []

import pytest
from pypara.monetary import Price

def test_price_neg_method():
    class TestPrice(Price):
        def __neg__(self):
            return self

    price_instance = TestPrice()
    neg_price = -price_instance

    assert neg_price is price_instance

