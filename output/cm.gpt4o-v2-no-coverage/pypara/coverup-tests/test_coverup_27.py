# file: pypara/monetary.py:1219-1224
# asked: {"lines": [1219, 1220, 1221, 1222, 1223, 1224], "branches": [[1220, 1221], [1220, 1222], [1222, 1223], [1222, 1224]]}
# gained: {"lines": [1219, 1220, 1221, 1222, 1223, 1224], "branches": [[1220, 1221], [1220, 1222], [1222, 1223], [1222, 1224]]}

import pytest
from decimal import Decimal
from datetime import date as Date
from pypara.currencies import Currency
from pypara.monetary import SomePrice, IncompatibleCurrencyError
from pypara.commons.zeitgeist import Date

class MockPrice:
    def __init__(self, ccy, qty, undefined=False):
        self.ccy = ccy
        self.qty = qty
        self.undefined = undefined

def test_someprice_lte_undefined(mocker):
    usd = mocker.Mock(spec=Currency)
    usd.code = "USD"
    price1 = SomePrice(ccy=usd, qty=Decimal("10.00"), dov=Date.today())
    price2 = MockPrice(ccy=usd, qty=Decimal("20.00"), undefined=True)
    
    assert not price1.lte(price2)

def test_someprice_lte_incompatible_currency(mocker):
    usd = mocker.Mock(spec=Currency)
    usd.code = "USD"
    eur = mocker.Mock(spec=Currency)
    eur.code = "EUR"
    price1 = SomePrice(ccy=usd, qty=Decimal("10.00"), dov=Date.today())
    price2 = MockPrice(ccy=eur, qty=Decimal("20.00"))
    
    with pytest.raises(IncompatibleCurrencyError):
        price1.lte(price2)

def test_someprice_lte_less_than(mocker):
    usd = mocker.Mock(spec=Currency)
    usd.code = "USD"
    price1 = SomePrice(ccy=usd, qty=Decimal("10.00"), dov=Date.today())
    price2 = MockPrice(ccy=usd, qty=Decimal("20.00"))
    
    assert price1.lte(price2)

def test_someprice_lte_equal(mocker):
    usd = mocker.Mock(spec=Currency)
    usd.code = "USD"
    price1 = SomePrice(ccy=usd, qty=Decimal("10.00"), dov=Date.today())
    price2 = MockPrice(ccy=usd, qty=Decimal("10.00"))
    
    assert price1.lte(price2)

def test_someprice_lte_greater_than(mocker):
    usd = mocker.Mock(spec=Currency)
    usd.code = "USD"
    price1 = SomePrice(ccy=usd, qty=Decimal("20.00"), dov=Date.today())
    price2 = MockPrice(ccy=usd, qty=Decimal("10.00"))
    
    assert not price1.lte(price2)
