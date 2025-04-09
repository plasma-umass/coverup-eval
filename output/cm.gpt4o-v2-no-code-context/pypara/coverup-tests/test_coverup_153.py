# file: pypara/monetary.py:1233-1238
# asked: {"lines": [1234, 1235, 1236, 1237, 1238], "branches": [[1234, 1235], [1234, 1236], [1236, 1237], [1236, 1238]]}
# gained: {"lines": [1234, 1235, 1236, 1237, 1238], "branches": [[1234, 1235], [1234, 1236], [1236, 1237], [1236, 1238]]}

import pytest
from decimal import Decimal
from pypara.monetary import SomePrice, Currency, IncompatibleCurrencyError
from datetime import date as Date

# Mock Currency class for testing purposes
class MockCurrency:
    def __init__(self, code):
        self.code = code

    def __eq__(self, other):
        if isinstance(other, MockCurrency):
            return self.code == other.code
        return False

def test_someprice_gte_with_undefined_other(monkeypatch):
    class MockPrice:
        undefined = True
        ccy = MockCurrency("USD")
        qty = Decimal("0.00")
    
    some_price = SomePrice(ccy=MockCurrency("USD"), qty=Decimal("10.00"), dov=Date.today())
    other_price = MockPrice()
    
    assert some_price.gte(other_price) is True

def test_someprice_gte_with_different_currency():
    some_price = SomePrice(ccy=MockCurrency("USD"), qty=Decimal("10.00"), dov=Date.today())
    other_price = SomePrice(ccy=MockCurrency("EUR"), qty=Decimal("5.00"), dov=Date.today())
    
    with pytest.raises(IncompatibleCurrencyError):
        some_price.gte(other_price)

def test_someprice_gte_with_same_currency():
    some_price = SomePrice(ccy=MockCurrency("USD"), qty=Decimal("10.00"), dov=Date.today())
    other_price = SomePrice(ccy=MockCurrency("USD"), qty=Decimal("5.00"), dov=Date.today())
    
    assert some_price.gte(other_price) is True

    other_price = SomePrice(ccy=MockCurrency("USD"), qty=Decimal("15.00"), dov=Date.today())
    
    assert some_price.gte(other_price) is False
