# file: pypara/monetary.py:1013-1020
# asked: {"lines": [1013, 1014, 1018, 1019, 1020], "branches": [[1018, 1019], [1018, 1020]]}
# gained: {"lines": [1013, 1014, 1018, 1019, 1020], "branches": [[1018, 1019], [1018, 1020]]}

import pytest
from decimal import Decimal
from pypara.monetary import Price, Currency, NoPrice, SomePrice
from datetime import date as Date

def test_price_of_with_none_values():
    assert Price.of(None, None, None) == NoPrice
    assert Price.of(Currency('USD', 'Dollar', 2, 'fiat', None, None), None, None) == NoPrice
    assert Price.of(None, Decimal('10.00'), None) == NoPrice
    assert Price.of(None, None, Date.today()) == NoPrice
    assert Price.of(Currency('USD', 'Dollar', 2, 'fiat', None, None), Decimal('10.00'), None) == NoPrice
    assert Price.of(Currency('USD', 'Dollar', 2, 'fiat', None, None), None, Date.today()) == NoPrice
    assert Price.of(None, Decimal('10.00'), Date.today()) == NoPrice

def test_price_of_with_valid_values():
    ccy = Currency('USD', 'Dollar', 2, 'fiat', None, None)
    qty = Decimal('10.00')
    dov = Date.today()
    price = Price.of(ccy, qty, dov)
    assert isinstance(price, SomePrice)
    assert price.ccy == ccy
    assert price.qty == qty
    assert price.dov == dov
