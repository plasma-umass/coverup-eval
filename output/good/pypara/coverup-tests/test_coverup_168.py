# file pypara/monetary.py:674-675
# lines [674, 675]
# branches []

import pytest
from pypara.monetary import NoneMoney

class MockMoney:
    def __init__(self, amount, currency):
        self.defined = True

def test_none_money_lt():
    none_money = NoneMoney()
    defined_money = MockMoney(10, 'USD')

    # Test that NoneMoney is less than defined Money
    assert none_money.lt(defined_money) is True

    # Test that NoneMoney is not less than another NoneMoney
    assert none_money.lt(NoneMoney()) is False

    # Clean up is not necessary as no external state is modified
