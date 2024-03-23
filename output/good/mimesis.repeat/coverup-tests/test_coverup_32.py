# file mimesis/builtins/en.py:25-52
# lines [25, 33, 35, 36, 38, 39, 43, 47, 51, 52]
# branches ['35->36', '35->38']

import pytest
from mimesis.builtins.en import USASpecProvider

@pytest.fixture
def usa_spec_provider():
    return USASpecProvider()

def test_tracking_number_usps(usa_spec_provider):
    tracking_number = usa_spec_provider.tracking_number(service='usps')
    assert tracking_number.startswith('1Z') or ' ' in tracking_number

def test_tracking_number_fedex(usa_spec_provider):
    tracking_number = usa_spec_provider.tracking_number(service='fedex')
    assert len(tracking_number.replace(' ', '')) in [12, 15]

def test_tracking_number_ups(usa_spec_provider):
    tracking_number = usa_spec_provider.tracking_number(service='ups')
    assert tracking_number.startswith('1Z')

def test_tracking_number_unsupported_service(usa_spec_provider):
    with pytest.raises(ValueError):
        usa_spec_provider.tracking_number(service='dhl')
