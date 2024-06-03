# file pypara/monetary.py:1054-1055
# lines [1055]
# branches []

import pytest
from pypara.monetary import Price

def test_price_rounding(mocker):
    # Mock the round method to ensure it gets called
    mock_round = mocker.patch.object(Price, 'round', return_value=Price())

    price = Price()
    rounded_price = round(price, 2)

    # Assert that the round method was called with the correct argument
    mock_round.assert_called_once_with(2)
    # Assert that the returned value is an instance of Price
    assert isinstance(rounded_price, Price)
