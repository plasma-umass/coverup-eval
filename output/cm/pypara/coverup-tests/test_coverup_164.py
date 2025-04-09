# file pypara/monetary.py:653-654
# lines [653, 654]
# branches []

import pytest
from pypara.monetary import NoneMoney, Money

# Assuming there is a Money class that looks something like this:
class SomeMoney(Money):
    def __init__(self, amount):
        self.amount = amount

    def add(self, other: "Money") -> "Money":
        if isinstance(other, NoneMoney):
            return self
        return SomeMoney(self.amount + other.amount)

# The test function to cover the missing lines in NoneMoney.add
def test_none_money_add():
    none_money = NoneMoney()
    some_money = SomeMoney(100)

    # Test adding NoneMoney to SomeMoney
    result = none_money.add(some_money)

    # Verify that the result is the same instance as some_money
    assert result is some_money

    # Verify that the amount has not changed
    assert result.amount == 100

# Run the test function if this file is executed directly (not recommended)
if __name__ == "__main__":
    pytest.main()
