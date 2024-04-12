# file pypara/monetary.py:632-633
# lines [632, 633]
# branches []

import pytest
from pypara.monetary import NoneMoney

class MockMoney:
    pass

def test_none_money_is_equal():
    none_money_instance = NoneMoney()
    other_none_money_instance = NoneMoney()
    other_money_instance = MockMoney()

    # Test is_equal with another NoneMoney instance
    assert none_money_instance.is_equal(other_none_money_instance) == True

    # Test is_equal with a different class instance
    assert none_money_instance.is_equal(other_money_instance) == False

    # Clean up is not necessary as no external resources or state changes are involved
