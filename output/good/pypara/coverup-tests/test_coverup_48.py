# file pypara/monetary.py:288-293
# lines [288, 289, 293]
# branches []

import pytest
from decimal import Decimal
from pypara.monetary import Money

class ConcreteMoney(Money):
    def with_qty(self, qty: Decimal) -> "Money":
        return ConcreteMoney()

@pytest.fixture
def mock_money(mocker):
    return mocker.patch('pypara.monetary.Money', autospec=True)

def test_with_qty(mock_money):
    money_instance = ConcreteMoney()
    qty = Decimal('10.00')
    new_money = money_instance.with_qty(qty)
    assert isinstance(new_money, Money)
