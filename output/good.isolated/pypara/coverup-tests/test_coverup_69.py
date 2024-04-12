# file pypara/monetary.py:783-793
# lines [783, 784, 793]
# branches []

import pytest
from pypara.monetary import Price

class ConcretePrice(Price):
    def __init__(self, value):
        self.value = value

    def as_boolean(self):
        return bool(self.value)

def test_price_as_boolean():
    # Test with value that should return True
    price_true = ConcretePrice(100)
    assert price_true.as_boolean() is True

    # Test with value that should return False
    price_false = ConcretePrice(0)
    assert price_false.as_boolean() is False

    # Test with undefined value (None) that should return False
    price_undefined = ConcretePrice(None)
    assert price_undefined.as_boolean() is False
