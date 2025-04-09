# file: pypara/monetary.py:994-1003
# asked: {"lines": [1003], "branches": []}
# gained: {"lines": [1003], "branches": []}

import pytest
from pypara.monetary import Price, Currency, Date
from typing import Optional

class MockCurrency(Currency):
    def __init__(self):
        pass

class TestPrice:
    def test_convert_not_implemented(self):
        class TestPriceImplementation(Price):
            def convert(self, to: Currency, asof: Optional[Date] = None, strict: bool = False) -> "Price":
                super().convert(to, asof, strict)
        
        test_price = TestPriceImplementation()
        with pytest.raises(NotImplementedError):
            test_price.convert(MockCurrency())
