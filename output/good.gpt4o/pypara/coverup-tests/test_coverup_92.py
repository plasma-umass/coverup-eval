# file pypara/monetary.py:1327-1328
# lines [1327, 1328]
# branches []

import pytest
from pypara.monetary import Price, NonePrice

def test_none_price_is_equal():
    none_price_instance = NonePrice()
    another_none_price_instance = NonePrice()
    different_price_instance = Price()

    # Test that NonePrice is equal to another NonePrice instance
    assert none_price_instance.is_equal(another_none_price_instance)

    # Test that NonePrice is not equal to a different Price instance
    assert not none_price_instance.is_equal(different_price_instance)

    # Test that NonePrice is not equal to an instance of a different class
    assert not none_price_instance.is_equal("some string")
