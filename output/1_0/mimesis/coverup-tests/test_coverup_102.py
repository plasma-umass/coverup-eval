# file mimesis/providers/business.py:71-76
# lines [71, 76]
# branches []

import pytest
from mimesis.providers.business import Business

def test_cryptocurrency_iso_code(mocker):
    # Mock the random.choice method to control its output
    mocker.patch(
        'mimesis.random.Random.choice',
        return_value='BTC'
    )

    business = Business()
    crypto_code = business.cryptocurrency_iso_code()

    # Assert that the returned value is a string
    assert isinstance(crypto_code, str)
    # Assert that the mocked method was called
    business.random.choice.assert_called()
