# file pypara/monetary.py:1005-1011
# lines [1011]
# branches []

import pytest
from pypara.monetary import Price
from decimal import Decimal
from unittest.mock import Mock

class ConcretePrice(Price):
    def __init__(self, money):
        self._money = money

    @property
    def money(self):
        return self._money

@pytest.fixture
def mock_money():
    mock = Mock()
    mock.amount = Decimal('10.00')
    mock.currency = 'USD'
    return mock

def test_price_money_not_implemented():
    with pytest.raises(NotImplementedError):
        Price().money

def test_concrete_price_money(mock_money):
    price = ConcretePrice(mock_money)
    assert price.money == mock_money
