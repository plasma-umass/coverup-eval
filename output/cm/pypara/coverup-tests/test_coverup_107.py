# file pypara/monetary.py:1159-1162
# lines [1159, 1161, 1162]
# branches []

import pytest
from decimal import Decimal
from pypara.monetary import SomePrice, Currency, Date

@pytest.fixture
def mock_currency(mocker):
    return mocker.Mock(spec=Currency)

@pytest.fixture
def mock_date(mocker):
    return mocker.Mock(spec=Date)

def test_scalar_add(mock_currency, mock_date):
    price = SomePrice(mock_currency, Decimal('100.00'), mock_date)
    result = price.scalar_add(10)
    assert result == SomePrice(mock_currency, Decimal('110.00'), mock_date)
