# file pypara/monetary.py:1278-1281
# lines [1278, 1279, 1280, 1281]
# branches []

import pytest
from decimal import Decimal
from datetime import date
from pypara.monetary import SomePrice, SomeMoney, Currency

@pytest.fixture
def currency_mock(mocker):
    currency = mocker.Mock(spec=Currency)
    currency.quantizer = Decimal('0.01')
    return currency

def test_some_price_money_property(currency_mock):
    # Given a SomePrice instance with mock currency, quantity, and date of value
    qty = Decimal('123.456')
    dov = date.today()
    some_price = SomePrice(currency_mock, qty, dov)

    # When accessing the money property
    result = some_price.money

    # Then the result should be a SomeMoney instance with quantized quantity
    expected_qty = qty.quantize(currency_mock.quantizer)
    assert isinstance(result, SomeMoney)
    assert result.ccy == currency_mock
    assert result.qty == expected_qty
    assert result.dov == dov
