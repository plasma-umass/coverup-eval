# file mimesis/providers/hardware.py:105-113
# lines [113]
# branches []

import pytest
from mimesis.providers.hardware import Hardware

# Mock the RAM_TYPES constant to ensure the test is deterministic
@pytest.fixture
def mock_ram_types(mocker):
    mock_ram_types = ['DDR3', 'DDR4']
    mocker.patch('mimesis.providers.hardware.RAM_TYPES', mock_ram_types)
    return mock_ram_types

# Test function to cover the ram_type method
def test_ram_type(mock_ram_types):
    hardware = Hardware()
    ram_type = hardware.ram_type()
    assert ram_type in mock_ram_types
