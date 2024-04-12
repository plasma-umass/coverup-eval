# file pypara/monetary.py:133-138
# lines [138]
# branches []

import pytest
from pypara.monetary import Money

class DummyMoney(Money):
    pass

def test_money_negative_not_implemented():
    dummy_money = DummyMoney()
    with pytest.raises(NotImplementedError):
        dummy_money.negative()
