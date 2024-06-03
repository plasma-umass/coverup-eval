# file pypara/monetary.py:1038-1040
# lines [1040]
# branches []

import pytest
from pypara.monetary import Price

def test_price_int_method():
    class ConcretePrice(Price):
        def __int__(self):
            return 100

    price_instance = ConcretePrice()
    assert int(price_instance) == 100

    with pytest.raises(TypeError):
        class IncompletePrice(Price):
            pass

        incomplete_price_instance = IncompletePrice()
        int(incomplete_price_instance)
