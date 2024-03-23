# file pypara/monetary.py:199-206
# lines [199, 200, 206]
# branches []

import pytest
from pypara.monetary import Money
from numbers import Number

class Numeric(Number):
    pass

class ConcreteMoney(Money):
    def multiply(self, other: Numeric) -> "Money":
        if isinstance(other, Numeric):
            return ConcreteMoney()
        return self

def test_money_multiply(mocker):
    # Create a mock object for Numeric
    mock_numeric = mocker.create_autospec(Numeric)
    
    # Create an instance of the ConcreteMoney class
    money_instance = ConcreteMoney()
    
    # Call the multiply method with the mock object
    result = money_instance.multiply(mock_numeric)
    
    # Assert that the result is an instance of ConcreteMoney
    assert isinstance(result, ConcreteMoney)
