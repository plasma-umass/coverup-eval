# file mimesis/providers/hardware.py:62-76
# lines [62, 70, 71, 72, 73, 74]
# branches []

import pytest
from mimesis.providers import Hardware

@pytest.fixture
def hardware_provider():
    return Hardware()

def test_cpu_frequency(hardware_provider):
    frequency = hardware_provider.cpu_frequency()
    # The frequency should be a string ending with 'GHz'
    assert isinstance(frequency, str)
    assert frequency.endswith('GHz')
    # The frequency value should be between 1.5 and 4.3
    value = float(frequency.replace('GHz', ''))
    assert 1.5 <= value <= 4.3
