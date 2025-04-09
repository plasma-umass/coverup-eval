# file: pypara/monetary.py:891-898
# asked: {"lines": [891, 892, 898], "branches": []}
# gained: {"lines": [891, 892, 898], "branches": []}

import pytest
from pypara.monetary import Price, Money, Numeric

class TestPrice:
    def test_times_not_implemented(self):
        class TestPriceImplementation(Price):
            def times(self, other: Numeric) -> "Money":
                super().times(other)
        
        price_instance = TestPriceImplementation()
        with pytest.raises(NotImplementedError):
            price_instance.times(10)
