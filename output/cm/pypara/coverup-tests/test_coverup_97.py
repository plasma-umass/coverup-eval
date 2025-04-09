# file pypara/dcc.py:253-274
# lines [253, 261, 270, 271, 274]
# branches []

import pytest
from decimal import Decimal
from datetime import date
from unittest.mock import Mock
from pypara.dcc import DCC

class Money:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __eq__(self, other):
        return self.currency == other.currency and self.amount == other.amount

@pytest.fixture
def mock_last_payment_date(mocker):
    return mocker.patch('pypara.dcc._last_payment_date', return_value=date(2021, 1, 1))

@pytest.fixture
def mock_next_payment_date(mocker):
    return mocker.patch('pypara.dcc._next_payment_date', return_value=date(2021, 7, 1))

@pytest.fixture
def mock_interest(mocker):
    return mocker.patch('pypara.dcc.DCC.interest', return_value=Money('USD', Decimal('100.00')))

def test_dcc_coupon(mock_last_payment_date, mock_next_payment_date, mock_interest):
    dcc = DCC('ACT/360', [], ['USD'], lambda start, end, freq: Decimal('0.5'))
    principal = Money('USD', Decimal('1000.00'))
    rate = Decimal('0.05')
    start = date(2020, 1, 1)
    asof = date(2021, 3, 1)
    end = date(2022, 1, 1)
    freq = Decimal('2')

    coupon = dcc.coupon(principal, rate, start, asof, end, freq)

    mock_last_payment_date.assert_called_once_with(start, asof, freq, None)
    mock_next_payment_date.assert_called_once_with(date(2021, 1, 1), freq, None)
    mock_interest.assert_called_once_with(principal, rate, date(2021, 1, 1), asof, date(2021, 7, 1), Decimal(freq))
    assert coupon == Money('USD', Decimal('100.00')), "The coupon value should be USD 100.00"
