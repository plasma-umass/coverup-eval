# file pypara/monetary.py:671-672
# lines [671, 672]
# branches []

import pytest
from pypara.monetary import Money, NoneMoney
from decimal import Decimal

@pytest.fixture
def none_money():
    return NoneMoney()

def test_none_money_floor_divide(none_money):
    result = none_money.floor_divide(Decimal('10.0'))
    assert isinstance(result, NoneMoney)
