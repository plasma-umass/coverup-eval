# file: pypara/monetary.py:1327-1328
# asked: {"lines": [1327, 1328], "branches": []}
# gained: {"lines": [1327, 1328], "branches": []}

import pytest
from pypara.monetary import NonePrice

def test_noneprice_is_equal_with_noneprice_instance():
    none_price_instance = NonePrice()
    assert none_price_instance.is_equal(NonePrice()) is True

def test_noneprice_is_equal_with_different_class_instance():
    none_price_instance = NonePrice()
    class DifferentClass:
        pass
    assert none_price_instance.is_equal(DifferentClass()) is False
