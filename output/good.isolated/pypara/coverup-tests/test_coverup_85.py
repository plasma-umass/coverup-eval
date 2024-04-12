# file pypara/monetary.py:823-828
# lines [823, 824, 828]
# branches []

import pytest
from pypara.monetary import Price

class ConcretePrice(Price):
    def __init__(self, value):
        self.value = value

    def positive(self):
        if self.value < 0:
            return ConcretePrice(-self.value)
        return self

@pytest.fixture
def negative_price():
    return ConcretePrice(-10)

@pytest.fixture
def positive_price():
    return ConcretePrice(10)

def test_positive_with_negative_value(negative_price):
    positive = negative_price.positive()
    assert isinstance(positive, Price)
    assert positive.value == 10

def test_positive_with_positive_value(positive_price):
    positive = positive_price.positive()
    assert positive is positive_price
    assert positive.value == 10
