# file: pypara/monetary.py:1327-1328
# asked: {"lines": [1327, 1328], "branches": []}
# gained: {"lines": [1327, 1328], "branches": []}

import pytest
from pypara.monetary import NonePrice

def test_noneprice_is_equal():
    none_price_instance = NonePrice()
    another_none_price_instance = NonePrice()
    different_class_instance = object()

    # Test when other is an instance of NonePrice
    assert none_price_instance.is_equal(another_none_price_instance) is True

    # Test when other is not an instance of NonePrice
    assert none_price_instance.is_equal(different_class_instance) is False
