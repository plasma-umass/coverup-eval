# file: pypara/monetary.py:830-836
# asked: {"lines": [836], "branches": []}
# gained: {"lines": [836], "branches": []}

import pytest
from pypara.monetary import Price

def test_price_round_not_implemented():
    class TestPrice(Price):
        pass

    test_price = TestPrice()
    with pytest.raises(NotImplementedError):
        test_price.round()

