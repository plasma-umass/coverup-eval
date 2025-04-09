# file: pypara/monetary.py:281-286
# asked: {"lines": [281, 282, 286], "branches": []}
# gained: {"lines": [281, 282], "branches": []}

import pytest
from abc import ABC, abstractmethod
from pypara.monetary import Currency

class Money(ABC):
    @abstractmethod
    def with_ccy(self, ccy: Currency) -> "Money":
        pass

def test_with_ccy_abstract_method():
    with pytest.raises(TypeError):
        money = Money()

def test_with_ccy_implementation():
    class ConcreteMoney(Money):
        def with_ccy(self, ccy: Currency) -> "Money":
            return self

    money = ConcreteMoney()
    currency = Currency(code="USD", name="US Dollar", decimals=2, type="fiat", quantizer=None, hashcache=None)
    result = money.with_ccy(currency)
    assert result is money
