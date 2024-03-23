# file mimesis/providers/address.py:30-37
# lines [30, 35, 36, 37]
# branches []

import pytest
from mimesis.providers.address import Address
from unittest.mock import patch

def test_address_init():
    with patch('mimesis.providers.BaseDataProvider._pull') as mock_pull:
        # Initialize Address without specifying a locale
        address = Address()
        
        # Check if the _pull method was called with 'address.json'
        mock_pull.assert_called_once_with('address.json')
        
        # Check if the locale is set to the default value
        assert address.locale == 'en'
