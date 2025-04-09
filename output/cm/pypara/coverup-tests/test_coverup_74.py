# file pypara/monetary.py:548-550
# lines [548, 549, 550]
# branches []

import pytest
from decimal import Decimal
from pypara.monetary import SomeMoney, Currency
from datetime import date

@pytest.fixture
def currency_mock(mocker):
    currency = mocker.Mock(spec=Currency)
    currency.quantizer = Decimal('0.01')
    return currency

def test_with_qty_changes_quantity_and_respects_quantizer(currency_mock):
    original_money = SomeMoney(currency_mock, Decimal('123.456'), date.today())
    new_qty = Decimal('789.12345')
    expected_qty = new_qty.quantize(currency_mock.quantizer)
    
    new_money = original_money.with_qty(new_qty)
    
    assert new_money.qty == expected_qty, "Quantity should be quantized according to the currency's quantizer"
    assert new_money.ccy == original_money.ccy, "Currency should remain unchanged"
    assert new_money.dov == original_money.dov, "Date of value should remain unchanged"
