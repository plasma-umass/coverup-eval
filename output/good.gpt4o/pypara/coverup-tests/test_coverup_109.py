# file pypara/monetary.py:1375-1376
# lines [1375, 1376]
# branches []

import pytest
from pypara.monetary import Price, NonePrice

def test_noneprice_lte():
    none_price = NonePrice()
    other_price = Price()

    # Test that NonePrice.lte always returns True
    assert none_price.lte(other_price) is True

    # Clean up if necessary (though in this case, there's nothing to clean up)
