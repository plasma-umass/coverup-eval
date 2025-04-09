# file pypara/monetary.py:1141-1157
# lines [1141, 1142, 1143, 1151, 1152, 1154, 1155, 1157]
# branches ['1142->1143', '1142->1145', '1154->1155', '1154->1157']

import pytest
from decimal import Decimal
from datetime import date as Date
from pypara.monetary import SomePrice, IncompatibleCurrencyError

class Currency:
    def __init__(self, code):
        self.code = code

    def __eq__(self, other):
        return self.code == other.code

@pytest.fixture
def some_price():
    return SomePrice(Currency('USD'), Decimal('100.00'), Date(2021, 1, 1))

@pytest.fixture
def another_price():
    return SomePrice(Currency('EUR'), Decimal('50.00'), Date(2020, 12, 31))

@pytest.fixture
def same_currency_price():
    return SomePrice(Currency('USD'), Decimal('200.00'), Date(2021, 2, 1))

def test_some_price_addition_with_undefined_other(mocker, some_price):
    other = mocker.Mock()
    other.undefined = True
    result = some_price.add(other)
    assert result == some_price

def test_some_price_addition_with_different_currency(some_price, another_price):
    with pytest.raises(IncompatibleCurrencyError) as exc_info:
        some_price.add(another_price)
    assert exc_info.value.ccy1 == some_price.ccy
    assert exc_info.value.ccy2 == another_price.ccy
    assert exc_info.value.operation == "addition"

def test_some_price_addition_with_same_currency(some_price, same_currency_price):
    result = some_price.add(same_currency_price)
    assert result.ccy == some_price.ccy
    assert result.qty == some_price.qty + same_currency_price.qty
    assert result.dov == same_currency_price.dov  # The later date should be chosen
