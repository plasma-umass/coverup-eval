# file pypara/monetary.py:1005-1011
# lines [1005, 1006, 1007, 1011]
# branches []

import pytest
from abc import ABC, abstractmethod
from pypara.monetary import Money

class TestPriceImplementation:
    def test_price_money_not_implemented(self):
        class Price(ABC):
            @property
            @abstractmethod
            def money(self) -> Money:
                raise NotImplementedError

        class ConcretePrice(Price):
            @property
            def money(self) -> Money:
                return super().money

        with pytest.raises(NotImplementedError):
            price_instance = ConcretePrice()
            _ = price_instance.money
