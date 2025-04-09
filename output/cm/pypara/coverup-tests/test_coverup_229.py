# file pypara/monetary.py:1022-1024
# lines [1024]
# branches []

import pytest
from pypara.monetary import Price

class ConcretePrice(Price):
    def __bool__(self) -> bool:
        return super().__bool__()

def test_price_bool():
    with pytest.raises(TypeError):
        bool(Price())
