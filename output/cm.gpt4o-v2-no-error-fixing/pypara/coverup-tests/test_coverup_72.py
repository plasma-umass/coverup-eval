# file: pypara/monetary.py:1375-1376
# asked: {"lines": [1375, 1376], "branches": []}
# gained: {"lines": [1375, 1376], "branches": []}

import pytest
from pypara.monetary import NonePrice, Price

def test_noneprice_lte():
    none_price = NonePrice()
    other_price = NonePrice()  # Using NonePrice as the other Price instance

    # Test that lte always returns True
    assert none_price.lte(other_price) is True

    # Clean up if necessary (not much to clean up in this simple case)
