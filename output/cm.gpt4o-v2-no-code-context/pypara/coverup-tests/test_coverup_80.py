# file: pypara/monetary.py:632-633
# asked: {"lines": [632, 633], "branches": []}
# gained: {"lines": [632], "branches": []}

import pytest
from pypara.monetary import Money
from typing import Any

class TestNoneMoney:
    def test_is_equal_with_none_money(self):
        class NoneMoney(Money):
            def is_equal(self, other: Any) -> bool:
                return other.__class__ is NoneMoney

        none_money_instance = NoneMoney()
        other_none_money_instance = NoneMoney()
        
        assert none_money_instance.is_equal(other_none_money_instance) is True

    def test_is_equal_with_different_class(self):
        class NoneMoney(Money):
            def is_equal(self, other: Any) -> bool:
                return other.__class__ is NoneMoney

        none_money_instance = NoneMoney()
        other_instance = Money()  # Assuming Money is a valid class in pypara.monetary
        
        assert none_money_instance.is_equal(other_instance) is False
