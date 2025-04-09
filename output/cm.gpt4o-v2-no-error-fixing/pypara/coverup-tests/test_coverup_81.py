# file: pypara/monetary.py:100-110
# asked: {"lines": [110], "branches": []}
# gained: {"lines": [110], "branches": []}

import pytest
from pypara.monetary import Money

def test_money_as_boolean_not_implemented():
    class TestMoney(Money):
        def as_boolean(self) -> bool:
            return super().as_boolean()

    test_money = TestMoney()
    
    with pytest.raises(NotImplementedError):
        test_money.as_boolean()
