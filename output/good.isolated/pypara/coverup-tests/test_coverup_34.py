# file pypara/monetary.py:313-320
# lines [313, 314, 318, 319, 320]
# branches ['318->319', '318->320']

import pytest
from decimal import Decimal
from datetime import date
from pypara.monetary import Money, NoMoney, SomeMoney
from typing import Optional

# Assuming Currency is a class defined within the pypara.monetary module
# If not, this will need to be adjusted to import the correct Currency class
from pypara.monetary import Currency

@pytest.fixture
def mock_currency(mocker):
    mock = mocker.MagicMock(spec=Currency)
    mock.code = 'USD'  # Assuming Currency has an attribute 'code'
    return mock

@pytest.fixture
def mock_date(mocker):
    return mocker.MagicMock(spec=date)

def test_money_of_with_none_values():
    assert Money.of(None, None, None) is NoMoney

def test_money_of_with_valid_values(mock_currency, mock_date):
    ccy = mock_currency
    qty = Decimal('10.00')
    dov = mock_date

    # Mock the quantize method to return the same Decimal for simplicity
    ccy.quantize.return_value = qty

    money = Money.of(ccy, qty, dov)

    assert isinstance(money, SomeMoney)
    # Assuming SomeMoney has attributes 'ccy', 'qty', and 'dov' to match the constructor
    assert money.ccy == ccy
    assert money.qty == qty
    assert money.dov == dov
    ccy.quantize.assert_called_once_with(qty)
