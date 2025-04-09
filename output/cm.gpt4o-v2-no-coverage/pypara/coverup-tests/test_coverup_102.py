# file: pypara/monetary.py:362-363
# asked: {"lines": [362, 363], "branches": []}
# gained: {"lines": [362, 363], "branches": []}

import pytest
from unittest.mock import Mock
from pypara.monetary import Money

class TestMoney:
    @pytest.fixture
    def money(self):
        class ConcreteMoney(Money):
            def round(self, ndigits: int = 0) -> 'Money':
                return self

        return ConcreteMoney()

    def test_round_no_digits(self, money):
        result = round(money)
        assert isinstance(result, Money)

    def test_round_with_digits(self, money):
        result = round(money, 2)
        assert isinstance(result, Money)
