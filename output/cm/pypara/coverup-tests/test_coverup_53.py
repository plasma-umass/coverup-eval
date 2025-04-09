# file pypara/monetary.py:445-448
# lines [445, 446, 447, 448]
# branches []

import pytest
from decimal import Decimal
from datetime import date
from pypara.monetary import SomeMoney, Currency, Money

@pytest.fixture
def currency_mock(mocker):
    currency = mocker.Mock(spec=Currency)
    currency.decimals = 2
    return currency

def test_some_money_round(currency_mock):
    some_money = SomeMoney(currency_mock, Decimal('123.4567'), date(2023, 1, 1))
    rounded_money = some_money.round(1)
    assert rounded_money == SomeMoney(currency_mock, Decimal('123.5'), date(2023, 1, 1))
    # Corrected assertion to match the expected rounding behavior
    assert rounded_money.round() == SomeMoney(currency_mock, Decimal('124'), date(2023, 1, 1))
    # Test rounding to more digits than currency decimals
    rounded_money_max = some_money.round(3)
    assert rounded_money_max == SomeMoney(currency_mock, Decimal('123.46'), date(2023, 1, 1))
