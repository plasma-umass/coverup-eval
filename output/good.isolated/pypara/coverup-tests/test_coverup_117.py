# file pypara/monetary.py:1192-1194
# lines [1192, 1193, 1194]
# branches []

import pytest
from decimal import Decimal
from datetime import date
from pypara.monetary import SomePrice, SomeMoney, Currency

@pytest.fixture
def mock_currency(mocker):
    mock = mocker.Mock(spec=Currency)
    mock.quantizer = Decimal('0.01')
    return mock

def test_some_price_times(mock_currency):
    some_price = SomePrice(mock_currency, Decimal('10.00'), date(2023, 1, 1))
    result = some_price.times(2)
    assert isinstance(result, SomeMoney)
    assert result.ccy == mock_currency
    assert result.qty == Decimal('20.00')
    assert result.dov == date(2023, 1, 1)
