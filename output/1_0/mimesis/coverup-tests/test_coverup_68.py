# file mimesis/providers/hardware.py:115-123
# lines [115, 123]
# branches []

import pytest
from mimesis.providers.hardware import Hardware

# Assuming RAM_SIZES is a constant defined in the module that we need to mock
RAM_SIZES = ['2GB', '4GB', '8GB', '16GB', '32GB', '64GB']

@pytest.fixture
def hardware_provider(mocker):
    mocker.patch('mimesis.providers.hardware.RAM_SIZES', RAM_SIZES)
    return Hardware()

def test_ram_size(hardware_provider):
    ram_size = hardware_provider.ram_size()
    assert ram_size in RAM_SIZES
