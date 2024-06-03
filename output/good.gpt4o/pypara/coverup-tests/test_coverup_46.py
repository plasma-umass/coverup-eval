# file pypara/monetary.py:302-311
# lines [302, 303, 311]
# branches []

from typing import Optional
import pytest
from unittest.mock import Mock
from pypara.monetary import Money, Currency, Date, FXRateLookupError

def test_money_convert_not_implemented():
    class TestMoney(Money):
        def convert(self, to: Currency, asof: Optional[Date] = None, strict: bool = False) -> "Money":
            super().convert(to, asof, strict)
    
    test_money = TestMoney()
    with pytest.raises(NotImplementedError):
        test_money.convert(Mock(spec=Currency), Mock(spec=Date), strict=False)
