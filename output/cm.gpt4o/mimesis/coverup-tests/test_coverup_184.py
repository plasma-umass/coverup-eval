# file mimesis/builtins/en.py:25-52
# lines [33, 35, 36, 38, 39, 43, 47, 51, 52]
# branches ['35->36', '35->38']

import pytest
from mimesis.builtins.en import USASpecProvider

def test_tracking_number_usps():
    provider = USASpecProvider()
    tracking_number = provider.tracking_number('usps')
    assert len(tracking_number.replace(' ', '').replace('US', '')) in [20, 13, 11]

def test_tracking_number_fedex():
    provider = USASpecProvider()
    tracking_number = provider.tracking_number('fedex')
    assert len(tracking_number.replace(' ', '')) in [12, 15]

def test_tracking_number_ups():
    provider = USASpecProvider()
    tracking_number = provider.tracking_number('ups')
    assert tracking_number.startswith('1Z')

def test_tracking_number_invalid_service():
    provider = USASpecProvider()
    with pytest.raises(ValueError, match='Unsupported post service'):
        provider.tracking_number('dhl')
