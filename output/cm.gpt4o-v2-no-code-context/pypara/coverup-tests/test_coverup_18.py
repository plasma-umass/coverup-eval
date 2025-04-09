# file: pypara/monetary.py:1005-1011
# asked: {"lines": [1005, 1006, 1007, 1011], "branches": []}
# gained: {"lines": [1005, 1006, 1007], "branches": []}

import pytest
from abc import ABC, abstractmethod
from pypara.monetary import Money

class TestPriceImplementation:
    def test_price_money_not_implemented(self):
        class Price(ABC):
            @property
            @abstractmethod
            def money(self) -> Money:
                """
                Returns the money representation of the price object.
                """
                raise NotImplementedError

        class ConcretePrice(Price):
            @property
            def money(self) -> Money:
                super().money

        price = ConcretePrice()
        with pytest.raises(NotImplementedError):
            _ = price.money
