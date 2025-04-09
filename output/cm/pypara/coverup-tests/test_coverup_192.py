# file pypara/dcc.py:277-293
# lines [277, 278]
# branches []

import datetime
from decimal import Decimal
import pytest
from pypara.dcc import DCCRegistry

class Money:
    def __init__(self, currency, quantity, date):
        self.currency = currency
        self.qty = quantity
        self.date = date

    @staticmethod
    def of(currency, quantity, date):
        return Money(currency, quantity, date)

class Currencies:
    USD = 'USD'

@pytest.fixture
def principal():
    return Money.of(Currencies.USD, Decimal(1000000), datetime.date.today())

def test_dcc_registry_machinery_interest(principal, mocker):
    start = datetime.date(2007, 12, 28)
    end = datetime.date(2008, 2, 28)
    rate = Decimal(0.01)
    dcc_machinery_mock = mocker.MagicMock()
    mocker.patch('pypara.dcc.DCCRegistry.find', return_value=dcc_machinery_mock)
    dcc_machinery_mock.calculate_fraction.return_value = Decimal('0.16942884946478')
    dcc_machinery_mock.interest.return_value = Money.of(Currencies.USD, Decimal('1694.29'), end)

    dcc = DCCRegistry.find("Act/Act")
    interest_amount = dcc.interest(principal, rate, start, end, end).qty
    assert interest_amount == Decimal('1694.29')

    dcc_machinery_mock.interest.return_value = Money.of(Currencies.USD, Decimal('0.00'), start)
    interest_amount_zero = dcc.interest(principal, rate, end, start, start).qty
    assert interest_amount_zero == Decimal('0.00')
