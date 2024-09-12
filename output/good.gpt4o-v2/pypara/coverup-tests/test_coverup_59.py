# file: pypara/dcc.py:239-251
# asked: {"lines": [239, 245, 246, 251], "branches": []}
# gained: {"lines": [239, 245, 246, 251], "branches": []}

import pytest
from decimal import Decimal
from pypara.commons.zeitgeist import Date
from pypara.monetary import Money
from pypara.dcc import DCC
from pypara.currencies import Currency, CurrencyType

@pytest.fixture
def dcc_instance(mocker):
    mocker.patch('pypara.dcc.DCC.calculate_fraction', return_value=Decimal('0.5'))
    return DCC(name="30/360", altnames=set(), currencies=set(), calculate_fraction_method=None)

@pytest.fixture
def usd_currency():
    return Currency.of("USD", "US Dollars", 2, CurrencyType.MONEY)

@pytest.fixture
def money_instance(usd_currency):
    return Money.of(usd_currency, Decimal('1000.00'), Date(2023, 1, 1))

def test_interest_with_end_date(dcc_instance, money_instance):
    principal = money_instance
    rate = Decimal('0.05')
    start = Date(2023, 1, 1)
    asof = Date(2023, 6, 30)
    end = Date(2023, 12, 31)
    interest = dcc_instance.interest(principal, rate, start, asof, end)
    assert interest == Money.of(principal.ccy, Decimal('25.00'), start)

def test_interest_without_end_date(dcc_instance, money_instance):
    principal = money_instance
    rate = Decimal('0.05')
    start = Date(2023, 1, 1)
    asof = Date(2023, 6, 30)
    interest = dcc_instance.interest(principal, rate, start, asof)
    assert interest == Money.of(principal.ccy, Decimal('25.00'), start)

def test_interest_with_frequency(dcc_instance, money_instance):
    principal = money_instance
    rate = Decimal('0.05')
    start = Date(2023, 1, 1)
    asof = Date(2023, 6, 30)
    freq = Decimal('2')
    interest = dcc_instance.interest(principal, rate, start, asof, freq=freq)
    assert interest == Money.of(principal.ccy, Decimal('25.00'), start)
