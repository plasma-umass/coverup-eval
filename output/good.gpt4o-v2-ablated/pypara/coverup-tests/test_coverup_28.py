# file: pypara/monetary.py:674-675
# asked: {"lines": [674, 675], "branches": []}
# gained: {"lines": [674, 675], "branches": []}

import pytest
from pypara.monetary import NoneMoney, Money

class TestNoneMoney:
    @pytest.fixture
    def none_money(self):
        return NoneMoney()

    @pytest.fixture
    def defined_money(self, mocker):
        mock_money = mocker.Mock(spec=Money)
        mock_money.defined = True
        return mock_money

    @pytest.fixture
    def undefined_money(self, mocker):
        mock_money = mocker.Mock(spec=Money)
        mock_money.defined = False
        return mock_money

    def test_lt_with_defined_money(self, none_money, defined_money):
        assert none_money.lt(defined_money) is True

    def test_lt_with_undefined_money(self, none_money, undefined_money):
        assert none_money.lt(undefined_money) is False
