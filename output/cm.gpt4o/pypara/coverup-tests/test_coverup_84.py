# file pypara/monetary.py:1324-1325
# lines [1324, 1325]
# branches []

import pytest
from pypara.monetary import Price

class TestNonePrice:
    def test_as_boolean(self):
        class NonePrice(Price):
            def as_boolean(self) -> bool:
                return False

        none_price = NonePrice()
        assert not none_price.as_boolean()
