# file: pypara/monetary.py:450-466
# asked: {"lines": [451, 452, 460, 461, 463, 464, 466], "branches": [[451, 452], [451, 454], [463, 464], [463, 466]]}
# gained: {"lines": [451, 452, 460, 461, 463, 464, 466], "branches": [[451, 452], [451, 454], [463, 464], [463, 466]]}

import pytest
from decimal import Decimal
from datetime import date as Date
from pypara.monetary import SomeMoney, Currency, IncompatibleCurrencyError

# Mock Currency class for testing
class MockCurrency:
    def __init__(self, code):
        self.code = code
        self.name = code
        self.decimals = 2
        self.type = "fiat"
        self.quantizer = Decimal("0.01")
        self.hashcache = None

    def __eq__(self, other):
        return isinstance(other, MockCurrency) and self.code == other.code

def test_add_undefined_other():
    class MockMoney:
        undefined = True

    some_money = SomeMoney(MockCurrency("USD"), Decimal("100.00"), Date(2023, 1, 1))
    other_money = MockMoney()
    
    result = some_money.add(other_money)
    
    assert result == some_money

def test_add_incompatible_currency():
    some_money = SomeMoney(MockCurrency("USD"), Decimal("100.00"), Date(2023, 1, 1))
    other_money = SomeMoney(MockCurrency("EUR"), Decimal("50.00"), Date(2023, 1, 2))
    
    with pytest.raises(IncompatibleCurrencyError):
        some_money.add(other_money)

def test_add_compatible_currency():
    some_money = SomeMoney(MockCurrency("USD"), Decimal("100.00"), Date(2023, 1, 1))
    other_money = SomeMoney(MockCurrency("USD"), Decimal("50.00"), Date(2023, 1, 2))
    
    result = some_money.add(other_money)
    
    assert result.ccy == MockCurrency("USD")
    assert result.qty == Decimal("150.00")
    assert result.dov == Date(2023, 1, 2)
