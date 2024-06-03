# file pypara/monetary.py:632-633
# lines [632, 633]
# branches []

import pytest
from pypara.monetary import Money
from typing import Any

class NoneMoney(Money):
    def is_equal(self, other: Any) -> bool:
        return other.__class__ is NoneMoney

def test_none_money_is_equal():
    none_money_instance = NoneMoney()
    another_none_money_instance = NoneMoney()
    different_money_instance = Money()

    # Test that two NoneMoney instances are considered equal
    assert none_money_instance.is_equal(another_none_money_instance) is True

    # Test that NoneMoney instance is not equal to a different Money instance
    assert none_money_instance.is_equal(different_money_instance) is False

    # Test that NoneMoney instance is not equal to an object of a different type
    assert none_money_instance.is_equal("not a money instance") is False
