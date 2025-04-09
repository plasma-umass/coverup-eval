# file pypara/monetary.py:342-344
# lines [344]
# branches []

import pytest
from pypara.monetary import Money

def test_money_float_abstract_method():
    with pytest.raises(TypeError):
        class TestMoney(Money):
            pass

        instance = TestMoney()
        float(instance)
