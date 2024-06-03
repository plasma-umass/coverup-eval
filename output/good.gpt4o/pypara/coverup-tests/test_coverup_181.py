# file pypara/monetary.py:1113-1114
# lines [1114]
# branches []

import pytest
from decimal import Decimal
from datetime import date as Date
from pypara.monetary import SomePrice, Currency

def test_someprice_is_equal():
    currency = Currency(code="USD", name="US Dollar", decimals=2, type="fiat", quantizer=Decimal("0.01"), hashcache=None)
    price1 = SomePrice(ccy=currency, qty=Decimal("100.00"), dov=Date(2023, 10, 1))
    price2 = SomePrice(ccy=currency, qty=Decimal("100.00"), dov=Date(2023, 10, 1))
    price3 = SomePrice(ccy=currency, qty=Decimal("200.00"), dov=Date(2023, 10, 1))
    price4 = "Not a SomePrice instance"

    # Test equality with same class and same values
    assert price1.is_equal(price2) is True

    # Test inequality with same class but different values
    assert price1.is_equal(price3) is False

    # Test inequality with different class
    assert price1.is_equal(price4) is False
