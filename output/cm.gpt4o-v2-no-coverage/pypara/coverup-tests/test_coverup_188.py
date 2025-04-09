# file: pypara/monetary.py:524-529
# asked: {"lines": [525, 526, 527, 528, 529], "branches": [[525, 526], [525, 527], [527, 528], [527, 529]]}
# gained: {"lines": [525, 526, 527, 528, 529], "branches": [[525, 526], [525, 527], [527, 528], [527, 529]]}

import pytest
from decimal import Decimal
from datetime import date as Date
from pypara.monetary import SomeMoney, IncompatibleCurrencyError
from pypara.currencies import Currency

class MockCurrency:
    def __init__(self, code, name, decimals):
        self.code = code
        self.name = name
        self.decimals = decimals

class MockMoney:
    def __init__(self, ccy, qty, undefined=False):
        self.ccy = ccy
        self.qty = qty
        self.undefined = undefined

def test_lte_with_undefined_other():
    ccy = MockCurrency("USD", "US Dollar", 2)
    some_money = SomeMoney(ccy=ccy, qty=Decimal("100.00"), dov=Date.today())
    other_money = MockMoney(ccy=ccy, qty=Decimal("50.00"), undefined=True)
    
    assert not some_money.lte(other_money)

def test_lte_with_incompatible_currency():
    ccy1 = MockCurrency("USD", "US Dollar", 2)
    ccy2 = MockCurrency("EUR", "Euro", 2)
    some_money = SomeMoney(ccy=ccy1, qty=Decimal("100.00"), dov=Date.today())
    other_money = MockMoney(ccy=ccy2, qty=Decimal("50.00"))
    
    with pytest.raises(IncompatibleCurrencyError) as excinfo:
        some_money.lte(other_money)
    
    assert str(excinfo.value) == "USD vs EUR are incompatible for operation '<= comparision'."

def test_lte_with_compatible_currency():
    ccy = MockCurrency("USD", "US Dollar", 2)
    some_money = SomeMoney(ccy=ccy, qty=Decimal("100.00"), dov=Date.today())
    other_money = MockMoney(ccy=ccy, qty=Decimal("150.00"))
    
    assert some_money.lte(other_money)
    
    other_money.qty = Decimal("50.00")
    assert not some_money.lte(other_money)
