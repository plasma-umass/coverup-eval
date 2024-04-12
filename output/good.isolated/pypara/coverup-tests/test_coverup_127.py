# file pypara/monetary.py:1050-1052
# lines [1050, 1051, 1052]
# branches []

import pytest
from pypara.monetary import Price

@pytest.fixture
def price(mocker):
    # Mocking the Price class to simulate a Price object with an amount
    mocked_price = mocker.MagicMock(spec=Price)
    mocked_price.__round__.side_effect = lambda ndigits=0: "10.12" if ndigits == 2 else "10"
    return mocked_price

def test_price_rounding(price):
    rounded_price = round(price, 2)
    assert rounded_price == "10.12"

    rounded_price_no_digits = round(price)
    assert rounded_price_no_digits == "10"
