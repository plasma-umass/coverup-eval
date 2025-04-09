# file pypara/monetary.py:816-821
# lines [821]
# branches []

import pytest
from pypara.monetary import Price

class DummyPrice(Price):
    pass

def test_price_negative_raises_not_implemented_error():
    dummy_price = DummyPrice()
    with pytest.raises(NotImplementedError):
        dummy_price.negative()
