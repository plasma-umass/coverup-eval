# file: pypara/monetary.py:1327-1328
# asked: {"lines": [1327, 1328], "branches": []}
# gained: {"lines": [1327, 1328], "branches": []}

import pytest
from pypara.monetary import NonePrice

def test_none_price_is_equal_with_none_price():
    none_price_instance = NonePrice()
    other_none_price_instance = NonePrice()
    assert none_price_instance.is_equal(other_none_price_instance) is True

def test_none_price_is_equal_with_different_class():
    none_price_instance = NonePrice()
    class DifferentClass:
        pass
    different_class_instance = DifferentClass()
    assert none_price_instance.is_equal(different_class_instance) is False
