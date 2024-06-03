# file pypara/monetary.py:629-630
# lines [629, 630]
# branches []

import pytest
from pypara.monetary import Money

class TestNoneMoney:
    def test_as_boolean(self):
        class NoneMoney(Money):
            def as_boolean(self) -> bool:
                return False

        none_money = NoneMoney()
        assert not none_money.as_boolean()
