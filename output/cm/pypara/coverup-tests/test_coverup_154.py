# file pypara/monetary.py:692-693
# lines [692, 693]
# branches []

import pytest
from pypara.monetary import NoneMoney, Money
from datetime import date

@pytest.fixture
def mock_date():
    return date(2023, 4, 1)

def test_none_money_with_dov(mock_date):
    none_money = NoneMoney()
    result = none_money.with_dov(mock_date)
    assert result is none_money, "with_dov should return self for NoneMoney instances"
