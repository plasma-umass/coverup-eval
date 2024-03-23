# file pypara/monetary.py:342-344
# lines [344]
# branches []

import pytest
from pypara.monetary import Money

class DummyMoney(Money):
    pass

def test_money_abstract_float_method():
    with pytest.raises(TypeError):
        float(DummyMoney())
