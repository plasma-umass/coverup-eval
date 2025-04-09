# file pypara/dcc.py:253-274
# lines [270, 271, 274]
# branches []

import pytest
from decimal import Decimal
from datetime import date as Date
from unittest.mock import patch
from pypara.dcc import DCC

class Money:
    def __init__(self, amount):
        self.amount = amount

    def __eq__(self, other):
        return self.amount == other.amount

@pytest.fixture
def mock_last_payment_date(mocker):
    return mocker.patch('pypara.dcc._last_payment_date')

@pytest.fixture
def mock_next_payment_date(mocker):
    return mocker.patch('pypara.dcc._next_payment_date')

@pytest.fixture
def mock_interest(mocker):
    return mocker.patch('pypara.dcc.DCC.interest')

def test_coupon(mock_last_payment_date, mock_next_payment_date, mock_interest):
    # Arrange
    dcc = DCC(name='Test', altnames=[], currencies=[], calculate_fraction_method=None)
    principal = Money(1000)
    rate = Decimal('0.05')
    start = Date(2020, 1, 1)
    asof = Date(2020, 6, 1)
    end = Date(2021, 1, 1)
    freq = Decimal('2')
    eom = None

    mock_last_payment_date.return_value = Date(2020, 1, 1)
    mock_next_payment_date.return_value = Date(2020, 7, 1)
    mock_interest.return_value = Money(25)

    # Act
    result = dcc.coupon(principal, rate, start, asof, end, freq, eom)

    # Assert
    mock_last_payment_date.assert_called_once_with(start, asof, freq, eom)
    mock_next_payment_date.assert_called_once_with(mock_last_payment_date.return_value, freq, eom)
    mock_interest.assert_called_once_with(principal, rate, mock_last_payment_date.return_value, asof, mock_next_payment_date.return_value, Decimal(freq))
    assert result == Money(25)
