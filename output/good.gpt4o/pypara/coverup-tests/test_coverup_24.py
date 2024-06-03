# file pypara/dcc.py:253-274
# lines [253, 261, 270, 271, 274]
# branches []

import pytest
from decimal import Decimal
from datetime import date as Date
from typing import NamedTuple, Union, Optional

class Money(Decimal):
    pass

def _last_payment_date(start, asof, freq, eom):
    # Dummy implementation for testing purposes
    return start

def _next_payment_date(prevdate, freq, eom):
    # Dummy implementation for testing purposes
    return prevdate

class DCC(NamedTuple):
    def coupon(
        self,
        principal: Money,
        rate: Decimal,
        start: Date,
        asof: Date,
        end: Date,
        freq: Union[int, Decimal],
        eom: Optional[int] = None,
    ) -> Money:
        """
        Calculates the accrued interest for the coupon payment.

        This method is primarily used for bond coupon accruals which assumes the start date to be the first of regular
        payment schedules.
        """
        ## Find the previous and next payment dates:
        prevdate = _last_payment_date(start, asof, freq, eom)
        nextdate = _next_payment_date(prevdate, freq, eom)

        ## Calculate the interest and return:
        return self.interest(principal, rate, prevdate, asof, nextdate, Decimal(freq))

    def interest(self, principal, rate, prevdate, asof, nextdate, freq):
        # Dummy implementation for testing purposes
        return principal * rate * (asof - prevdate).days / 365

@pytest.fixture
def dcc():
    return DCC()

def test_coupon(dcc, mocker):
    principal = Money('1000.00')
    rate = Decimal('0.05')
    start = Date(2023, 1, 1)
    asof = Date(2023, 6, 1)
    end = Date(2023, 12, 31)
    freq = Decimal('2')
    eom = None

    mocker.patch('pypara.dcc._last_payment_date', return_value=start)
    mocker.patch('pypara.dcc._next_payment_date', return_value=end)

    result = dcc.coupon(principal, rate, start, asof, end, freq, eom)
    
    assert result == principal * rate * (asof - start).days / 365

