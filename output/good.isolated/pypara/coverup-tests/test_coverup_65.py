# file pypara/monetary.py:369-371
# lines [369, 370, 371]
# branches []

import pytest
from pypara.monetary import Money

class ConcreteMoney(Money):
    def __pos__(self) -> "Money":
        return self

def test_money_pos_operator():
    # Instantiate a concrete instance of the Money class
    concrete_money = ConcreteMoney()
    # Call the __pos__ method
    result = +concrete_money
    # Assert that the result is the concrete_money instance itself
    assert result is concrete_money
