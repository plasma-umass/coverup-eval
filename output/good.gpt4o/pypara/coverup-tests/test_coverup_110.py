# file pypara/monetary.py:1378-1379
# lines [1378, 1379]
# branches []

import pytest
from pypara.monetary import Price

class NonePrice(Price):
    def gt(self, other: "Price") -> bool:
        return False

def test_noneprice_gt():
    none_price = NonePrice()
    other_price = Price()

    # Assert that NonePrice's gt method always returns False
    assert not none_price.gt(other_price)
