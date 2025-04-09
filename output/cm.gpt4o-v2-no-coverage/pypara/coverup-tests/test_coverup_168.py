# file: pypara/monetary.py:1324-1325
# asked: {"lines": [1324, 1325], "branches": []}
# gained: {"lines": [1324, 1325], "branches": []}

import pytest
from pypara.monetary import NonePrice

def test_none_price_as_boolean():
    none_price = NonePrice()
    assert not none_price.as_boolean()

def test_none_price_is_equal():
    none_price = NonePrice()
    assert none_price.is_equal(NonePrice())
    assert not none_price.is_equal(10)

def test_none_price_abs():
    none_price = NonePrice()
    assert none_price.abs() == none_price

def test_none_price_as_float():
    none_price = NonePrice()
    with pytest.raises(TypeError, match="Undefined monetary values do not have quantity information."):
        none_price.as_float()

def test_none_price_as_integer():
    none_price = NonePrice()
    with pytest.raises(TypeError, match="Undefined monetary values do not have quantity information."):
        none_price.as_integer()

def test_none_price_round():
    none_price = NonePrice()
    assert none_price.round() == none_price

def test_none_price_negative():
    none_price = NonePrice()
    assert none_price.negative() == none_price

def test_none_price_positive():
    none_price = NonePrice()
    assert none_price.positive() == none_price

def test_none_price_add():
    none_price = NonePrice()
    assert none_price.add(NonePrice()) == none_price

def test_none_price_scalar_add():
    none_price = NonePrice()
    assert none_price.scalar_add(10) == none_price

def test_none_price_subtract():
    none_price = NonePrice()
    assert none_price.subtract(NonePrice()) == none_price

def test_none_price_scalar_subtract():
    none_price = NonePrice()
    assert none_price.scalar_subtract(10) == none_price

def test_none_price_multiply():
    none_price = NonePrice()
    assert none_price.multiply(10) == none_price

def test_none_price_times():
    none_price = NonePrice()
    assert none_price.times(10) == NonePrice.money

def test_none_price_divide():
    none_price = NonePrice()
    assert none_price.divide(10) == none_price

def test_none_price_floor_divide():
    none_price = NonePrice()
    assert none_price.floor_divide(10) == none_price

def test_none_price_lt():
    none_price = NonePrice()
    assert not none_price.lt(NonePrice())

def test_none_price_lte():
    none_price = NonePrice()
    assert none_price.lte(NonePrice())

def test_none_price_gt():
    none_price = NonePrice()
    assert not none_price.gt(NonePrice())

def test_none_price_gte():
    none_price = NonePrice()
    assert none_price.gte(NonePrice())

def test_none_price_with_ccy():
    none_price = NonePrice()
    from pypara.currencies import Currency, CurrencyType
    ccy = Currency.of('USD', 'US Dollars', 2, CurrencyType.MONEY)
    assert none_price.with_ccy(ccy) == none_price

def test_none_price_with_qty():
    none_price = NonePrice()
    from decimal import Decimal
    qty = Decimal('10.0')
    assert none_price.with_qty(qty) == none_price

def test_none_price_with_dov():
    none_price = NonePrice()
    from pypara.commons.zeitgeist import Date
    dov = Date.today()
    assert none_price.with_dov(dov) == none_price

def test_none_price_convert():
    none_price = NonePrice()
    from pypara.currencies import Currency, CurrencyType
    to_currency = Currency.of('EUR', 'Euro', 2, CurrencyType.MONEY)
    assert none_price.convert(to_currency) == none_price
