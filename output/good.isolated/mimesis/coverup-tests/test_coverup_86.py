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
        
        # Check if the _pull method was called with the correct datafile
        mock_pull.assert_called_once_with('address.json')
        
        # Since no locale was specified, the default should be 'en'
        assert address.locale == 'en'
