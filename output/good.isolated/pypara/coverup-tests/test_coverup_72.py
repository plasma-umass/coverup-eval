# file pypara/monetary.py:441-443
# lines [441, 442, 443]
# branches []

import pytest
from decimal import Decimal
from datetime import date
from pypara.monetary import SomeMoney, Currency

@pytest.fixture
def mock_currency(mocker):
    return mocker.MagicMock(spec=Currency)

@pytest.fixture
def mock_date(mocker):
    return mocker.MagicMock(spec=date)

def test_some_money_positive(mock_currency, mock_date):
    qty = Decimal('-10')
    some_money = SomeMoney(mock_currency, qty, mock_date)
    positive_money = some_money.positive()

    assert positive_money.qty == qty.__pos__(), "The quantity should be positive after calling positive()"
    assert positive_money.ccy == some_money.ccy, "The currency should remain unchanged after calling positive()"
    assert positive_money.dov == some_money.dov, "The date of value should remain unchanged after calling positive()"
