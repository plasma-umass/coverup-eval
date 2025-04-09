# file pypara/monetary.py:346-348
# lines [348]
# branches []

import pytest
from pypara.monetary import Money

def test_money_int_abstract_method():
    with pytest.raises(TypeError):
        class TestMoney(Money):
            pass

        test_money = TestMoney()
        int(test_money)
