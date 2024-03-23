# file mimesis/providers/hardware.py:145-153
# lines [153]
# branches []

import pytest
from mimesis.providers.hardware import Hardware

# Assuming MANUFACTURERS is a constant list of manufacturers in the same module
from mimesis.providers.hardware import MANUFACTURERS

@pytest.fixture
def hardware_provider():
    return Hardware()

def test_manufacturer(hardware_provider):
    manufacturer = hardware_provider.manufacturer()
    assert manufacturer in MANUFACTURERS
