# file pypara/monetary.py:823-828
# lines [828]
# branches []

import pytest
from pypara.monetary import Price

class DummyPrice(Price):
    def positive(self) -> "Price":
        return self

def test_price_positive_not_implemented():
    class TestPrice(Price):
        pass

    with pytest.raises(NotImplementedError):
        TestPrice().positive()
