# file pypara/monetary.py:987-992
# lines [987, 988, 992]
# branches []

import pytest
from pypara.monetary import Price
from datetime import date

class ConcretePrice(Price):
    def __init__(self, value, defined=True):
        self.value = value
        self.defined = defined

    def with_dov(self, dov: date) -> "ConcretePrice":
        if self.defined:
            return ConcretePrice(self.value, self.defined)
        return self

def test_price_with_dov(mocker):
    # Create a concrete instance of the abstract Price class
    concrete_price_defined = ConcretePrice(100, defined=True)
    concrete_price_undefined = ConcretePrice(100, defined=False)

    # Define a Date of Value
    dov = date.today()

    # Test with defined price
    new_price_defined = concrete_price_defined.with_dov(dov)
    assert new_price_defined is not concrete_price_defined
    assert new_price_defined.value == concrete_price_defined.value
    assert new_price_defined.defined == concrete_price_defined.defined

    # Test with undefined price
    new_price_undefined = concrete_price_undefined.with_dov(dov)
    assert new_price_undefined is concrete_price_undefined
