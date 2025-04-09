# file: pypara/dcc.py:23-27
# asked: {"lines": [23, 27], "branches": []}
# gained: {"lines": [23, 27], "branches": []}

import pytest
from pypara.dcc import _as_ccys, Currency, Currencies

def test_as_ccys(monkeypatch):
    # Mocking the Currency class to ensure controlled test environment
    class MockCurrency:
        def __init__(self, code, name):
            self.code = code
            self.name = name

        def __eq__(self, other):
            return self.code == other.code and self.name == other.name

        def __hash__(self):
            return hash((self.code, self.name))

    # Mocking the Currencies dictionary
    mock_currencies = {
        'USD': MockCurrency('USD', 'United States Dollar'),
        'EUR': MockCurrency('EUR', 'Euro'),
        'JPY': MockCurrency('JPY', 'Japanese Yen')
    }
    
    monkeypatch.setattr('pypara.dcc.Currencies', mock_currencies)
    
    # Test input
    codes = {'USD', 'EUR'}
    
    # Expected output
    expected_output = {mock_currencies['USD'], mock_currencies['EUR']}
    
    # Call the function and assert the result
    result = _as_ccys(codes)
    assert result == expected_output

    # Clean up is handled by monkeypatch automatically
