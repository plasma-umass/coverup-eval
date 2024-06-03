# file pypara/monetary.py:683-684
# lines [683, 684]
# branches []

import pytest
from pypara.monetary import Money

class NoneMoney(Money):
    def gte(self, other: "Money") -> bool:
        return other.undefined

class TestNoneMoney:
    def test_gte_with_undefined_other(self, mocker):
        # Mocking the Money class to create an instance with undefined attribute
        other_money = mocker.Mock(spec=Money)
        other_money.undefined = True

        # Creating an instance of NoneMoney
        none_money = NoneMoney()

        # Asserting that gte method returns True when other.undefined is True
        assert none_money.gte(other_money) is True

    def test_gte_with_defined_other(self, mocker):
        # Mocking the Money class to create an instance with undefined attribute
        other_money = mocker.Mock(spec=Money)
        other_money.undefined = False

        # Creating an instance of NoneMoney
        none_money = NoneMoney()

        # Asserting that gte method returns False when other.undefined is False
        assert none_money.gte(other_money) is False
