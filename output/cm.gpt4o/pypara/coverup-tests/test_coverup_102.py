# file pypara/monetary.py:686-687
# lines [686, 687]
# branches []

import pytest
from pypara.monetary import Money, Currency

class TestNoneMoney:
    def test_with_ccy(self):
        class NoneMoney(Money):
            def with_ccy(self, ccy: Currency) -> "Money":
                return self

        none_money = NoneMoney()
        currency = Currency(code="USD", name="US Dollar", decimals=2, type="fiat", quantizer=None, hashcache=None)
        result = none_money.with_ccy(currency)
        
        assert result is none_money
