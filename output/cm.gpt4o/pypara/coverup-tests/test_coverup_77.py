# file pypara/dcc.py:23-27
# lines [23, 27]
# branches []

import pytest
from pypara.dcc import _as_ccys, Currency, Currencies

def test_as_ccys(mocker):
    # Mock the Currency class to control the test environment
    MockCurrency = mocker.create_autospec(Currency, instance=True)
    mock_currencies = {
        'USD': MockCurrency,
        'EUR': MockCurrency,
        'JPY': MockCurrency
    }
    mocker.patch('pypara.dcc.Currencies', mock_currencies)

    # Test input set of currency codes
    input_codes = {'USD', 'EUR'}
    
    # Expected output set of Currency objects
    expected_output = {mock_currencies['USD'], mock_currencies['EUR']}
    
    # Call the function and assert the result
    result = _as_ccys(input_codes)
    assert result == expected_output

    # Clean up: No explicit cleanup needed as mocker handles it
