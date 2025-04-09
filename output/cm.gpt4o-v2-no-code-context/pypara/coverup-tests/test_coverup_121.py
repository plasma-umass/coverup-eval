# file: pypara/monetary.py:126-131
# asked: {"lines": [131], "branches": []}
# gained: {"lines": [131], "branches": []}

import pytest
from pypara.monetary import Money

def test_money_abs_not_implemented():
    class TestMoney(Money):
        pass

    test_money = TestMoney()
    
    with pytest.raises(NotImplementedError):
        test_money.abs()
