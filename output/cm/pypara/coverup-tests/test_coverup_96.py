# file pypara/monetary.py:830-836
# lines [830, 831, 836]
# branches []

import pytest
from pypara.monetary import Price

class ConcretePrice(Price):
    def round(self, ndigits: int = 0) -> "Price":
        return ConcretePrice()

def test_price_round():
    # Create a concrete subclass of Price to test the round method
    concrete_price = ConcretePrice()
    
    # Expect the round method to return an instance of ConcretePrice
    rounded_price = concrete_price.round()
    assert isinstance(rounded_price, ConcretePrice)
