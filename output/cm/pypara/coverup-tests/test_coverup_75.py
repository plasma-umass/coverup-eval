# file pypara/monetary.py:771-781
# lines [771, 772, 781]
# branches []

import pytest
from pypara.monetary import Price

class ConcretePrice(Price):
    __slots__ = ('value',)

    def __init__(self, value):
        self.value = value

    def is_equal(self, other):
        if isinstance(other, ConcretePrice):
            return all(getattr(self, slot) == getattr(other, slot) for slot in self.__slots__)
        return False

@pytest.fixture
def price():
    return ConcretePrice(10)

@pytest.fixture
def other_price():
    return ConcretePrice(10)

@pytest.fixture
def different_price():
    return ConcretePrice(20)

def test_price_is_equal(price, other_price, different_price):
    assert price.is_equal(other_price), "The prices should be equal"
    assert not price.is_equal(different_price), "The prices should not be equal"
    assert not price.is_equal(None), "The comparison should return False when other is not a Price instance"
    assert not price.is_equal(10), "The comparison should return False when other is not a Price instance"
