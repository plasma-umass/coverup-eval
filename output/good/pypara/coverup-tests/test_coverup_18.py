# file pypara/monetary.py:621-628
# lines [621, 623, 625, 627]
# branches []

import pytest
from pypara.monetary import NoneMoney, Money

def test_none_money():
    none_money = NoneMoney()
    
    assert none_money.defined is False
    assert none_money.undefined is True
    assert isinstance(none_money, Money)
    assert isinstance(none_money, NoneMoney)
