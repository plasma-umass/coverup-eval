# file pypara/monetary.py:1378-1379
# lines [1379]
# branches []

import pytest
from pypara.monetary import Price, NonePrice

def test_none_price_gt():
    none_price = NonePrice()
    other_price = Price()  # Assuming Price can be initialized without arguments

    # Test that NonePrice's gt method always returns False
    assert none_price.gt(other_price) is False

    # Clean up if necessary (not needed in this simple case)
