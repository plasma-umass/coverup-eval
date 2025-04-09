# file pypara/monetary.py:330-332
# lines [332]
# branches []

import pytest
from pypara.monetary import Money

def test_money_bool_abstract_method():
    with pytest.raises(TypeError):
        class TestMoney(Money):
            pass

        test_money_instance = TestMoney()
        bool(test_money_instance)
