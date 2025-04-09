# file pypara/monetary.py:739-770
# lines [739, 740, 745, 748, 753, 758, 763, 766, 769]
# branches []

import pytest
from decimal import Decimal
from datetime import date as Date
from pypara.monetary import Price

class MockCurrency:
    def __init__(self, code):
        self.code = code

class DefinedPrice(Price):
    def __init__(self, ccy, qty, dov):
        self._ccy = ccy
        self._qty = qty
        self._dov = dov

    @property
    def ccy(self):
        return self._ccy

    @property
    def qty(self):
        return self._qty

    @property
    def dov(self):
        return self._dov

    @property
    def defined(self):
        return True

    @property
    def undefined(self):
        return not self.defined

class UndefinedPrice(Price):
    @property
    def ccy(self):
        raise TypeError("Undefined price has no currency")

    @property
    def qty(self):
        raise TypeError("Undefined price has no quantity")

    @property
    def dov(self):
        raise TypeError("Undefined price has no date of value")

    @property
    def defined(self):
        return False

    @property
    def undefined(self):
        return not self.defined

def test_defined_price():
    ccy = MockCurrency('USD')
    qty = Decimal('100.00')
    dov = Date.today()
    price = DefinedPrice(ccy, qty, dov)

    assert price.ccy == ccy
    assert price.qty == qty
    assert price.dov == dov
    assert price.defined is True
    assert price.undefined is False

def test_undefined_price():
    price = UndefinedPrice()

    with pytest.raises(TypeError):
        _ = price.ccy
    with pytest.raises(TypeError):
        _ = price.qty
    with pytest.raises(TypeError):
        _ = price.dov

    assert price.defined is False
    assert price.undefined is True
