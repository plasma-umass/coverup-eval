# file pypara/monetary.py:668-669
# lines [668, 669]
# branches []

import pytest
from pypara.monetary import Money, NoneMoney
from decimal import Decimal

@pytest.fixture
def none_money():
    return NoneMoney()

def test_none_money_divide(none_money):
    result = none_money.divide(Decimal('2'))
    assert isinstance(result, NoneMoney), "The result should be an instance of NoneMoney"
