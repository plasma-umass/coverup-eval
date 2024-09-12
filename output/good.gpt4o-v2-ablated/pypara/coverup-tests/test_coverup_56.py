# file: pypara/monetary.py:1164-1180
# asked: {"lines": [1165, 1166, 1174, 1175, 1177, 1178, 1180], "branches": [[1165, 1166], [1165, 1168], [1177, 1178], [1177, 1180]]}
# gained: {"lines": [1165, 1166, 1174, 1175, 1177, 1178, 1180], "branches": [[1165, 1166], [1165, 1168], [1177, 1178], [1177, 1180]]}

import pytest
from decimal import Decimal
from datetime import date as Date
from pypara.monetary import SomePrice, Currency, IncompatibleCurrencyError

class MockCurrency:
    def __init__(self, code):
        self.code = code

    def __eq__(self, other):
        return self.code == other.code

    def __ne__(self, other):
        return self.code != other.code

class MockPrice:
    def __init__(self, ccy, qty, dov, undefined=False):
        self.ccy = ccy
        self.qty = qty
        self.dov = dov
        self.undefined = undefined

    def __iter__(self):
        return iter((self.ccy, self.qty, self.dov))

def test_subtract_undefined_price():
    ccy = MockCurrency("USD")
    price1 = SomePrice(ccy, Decimal("100.00"), Date(2023, 1, 1))
    undefined_price = MockPrice(ccy, Decimal("0.00"), Date(2023, 1, 1), undefined=True)
    
    result = price1.subtract(undefined_price)
    
    assert result == price1

def test_subtract_incompatible_currency():
    ccy1 = MockCurrency("USD")
    ccy2 = MockCurrency("EUR")
    price1 = SomePrice(ccy1, Decimal("100.00"), Date(2023, 1, 1))
    price2 = MockPrice(ccy2, Decimal("50.00"), Date(2023, 1, 1))
    
    with pytest.raises(IncompatibleCurrencyError):
        price1.subtract(price2)

def test_subtract_same_currency():
    ccy = MockCurrency("USD")
    price1 = SomePrice(ccy, Decimal("100.00"), Date(2023, 1, 1))
    price2 = MockPrice(ccy, Decimal("50.00"), Date(2023, 1, 2))
    
    result = price1.subtract(price2)
    
    assert result.ccy == ccy
    assert result.qty == Decimal("50.00")
    assert result.dov == Date(2023, 1, 2)

def test_subtract_same_currency_earlier_date():
    ccy = MockCurrency("USD")
    price1 = SomePrice(ccy, Decimal("100.00"), Date(2023, 1, 2))
    price2 = MockPrice(ccy, Decimal("50.00"), Date(2023, 1, 1))
    
    result = price1.subtract(price2)
    
    assert result.ccy == ccy
    assert result.qty == Decimal("50.00")
    assert result.dov == Date(2023, 1, 2)
