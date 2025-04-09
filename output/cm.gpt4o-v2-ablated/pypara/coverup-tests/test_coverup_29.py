# file: pypara/monetary.py:683-684
# asked: {"lines": [683, 684], "branches": []}
# gained: {"lines": [683, 684], "branches": []}

import pytest
from pypara.monetary import NoneMoney, Money

class TestNoneMoney:
    @pytest.fixture
    def none_money(self):
        return NoneMoney()

    @pytest.fixture
    def mock_money(self, mocker):
        mock_money = mocker.Mock(spec=Money)
        mock_money.undefined = True
        return mock_money

    def test_gte_with_undefined(self, none_money, mock_money):
        assert none_money.gte(mock_money) is True

    def test_gte_with_defined(self, none_money, mocker):
        mock_money = mocker.Mock(spec=Money)
        mock_money.undefined = False
        assert none_money.gte(mock_money) is False
