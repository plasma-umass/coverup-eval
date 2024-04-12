# file pypara/monetary.py:686-687
# lines [686, 687]
# branches []

import pytest
from pypara.monetary import NoneMoney, Currency, Money

class MockCurrency(Currency):
    def __init__(self, code):
        super().__init__(code, "Mock Currency", 2, "fiat", lambda x: x, True)

def test_none_money_with_ccy():
    none_money = NoneMoney()
    currency = MockCurrency(code="USD")
    
    # Call with_ccy and assert it returns self
    result = none_money.with_ccy(currency)
    assert result is none_money, "with_ccy should return self for NoneMoney instances"
