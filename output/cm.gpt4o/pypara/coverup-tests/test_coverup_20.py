# file pypara/monetary.py:1102-1112
# lines [1102, 1103, 1107, 1109, 1111]
# branches []

import pytest
from decimal import Decimal
from datetime import date as Date
from pypara.monetary import Currency, Price, SomePrice

def test_someprice_initialization():
    ccy = Currency(code="USD", name="US Dollar", decimals=2, type="fiat", quantizer=Decimal("0.01"), hashcache=None)
    qty = Decimal("100.00")
    dov = Date(2023, 10, 1)
    
    price = SomePrice(ccy=ccy, qty=qty, dov=dov)
    
    assert price.ccy == ccy
    assert price.qty == qty
    assert price.dov == dov
    assert price.defined is True
    assert price.undefined is False
