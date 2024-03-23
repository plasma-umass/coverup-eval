# file pypara/monetary.py:1113-1114
# lines [1113, 1114]
# branches []

import pytest
from decimal import Decimal
from datetime import date
from pypara.monetary import SomePrice, Currency

@pytest.fixture
def cleanup():
    # Setup code if necessary
    yield
    # Cleanup code if necessary

def test_SomePrice_is_equal(cleanup, mocker):
    # Assuming Currency and Date are classes that need to be mocked for this test
    CurrencyMock = mocker.MagicMock(spec=Currency)
    DateMock = mocker.MagicMock(spec=date)

    currency1 = CurrencyMock()
    currency2 = CurrencyMock()
    date1 = DateMock()
    date2 = DateMock()

    price1 = SomePrice(ccy=currency1, qty=Decimal('10.00'), dov=date1)
    price2 = SomePrice(ccy=currency1, qty=Decimal('10.00'), dov=date1)
    price3 = SomePrice(ccy=currency2, qty=Decimal('20.00'), dov=date2)
    price4 = "not_a_price_instance"

    assert price1.is_equal(price2), "price1 should be equal to price2"
    assert not price1.is_equal(price3), "price1 should not be equal to price3"
    assert not price1.is_equal(price4), "price1 should not be equal to a non-Price instance"
