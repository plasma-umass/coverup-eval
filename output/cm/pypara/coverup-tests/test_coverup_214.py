# file pypara/monetary.py:346-348
# lines [348]
# branches []

import pytest
from pypara.monetary import Money

class ConcreteMoney(Money):
    def __int__(self):
        return super().__int__()

def test_money_abstract_int_method():
    with pytest.raises(TypeError):
        _ = int(Money())
