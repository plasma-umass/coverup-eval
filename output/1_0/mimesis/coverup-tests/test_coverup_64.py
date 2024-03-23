# file mimesis/providers/hardware.py:95-103
# lines [95, 103]
# branches []

import pytest
from mimesis.providers.hardware import Hardware

# Assuming CPU_CODENAMES is a list of codenames in the actual mimesis.providers.hardware module
CPU_CODENAMES = ['Cannonlake', 'Icelake', 'Tigerlake', 'Sapphire Rapids']

# Mocking the CPU_CODENAMES in the hardware module
@pytest.fixture(autouse=True)
def mock_cpu_codenames(mocker):
    mocker.patch('mimesis.providers.hardware.CPU_CODENAMES', new=CPU_CODENAMES)

def test_cpu_codename():
    hardware = Hardware()
    codename = hardware.cpu_codename()
    assert codename in CPU_CODENAMES
