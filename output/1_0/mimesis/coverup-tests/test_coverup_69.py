# file mimesis/providers/hardware.py:135-143
# lines [135, 143]
# branches []

import pytest
from mimesis.providers.hardware import Hardware

# Assuming GRAPHICS is a constant list defined in the hardware module
# If it's not, you would need to mock it or define it for the test
from mimesis.providers.hardware import GRAPHICS


@pytest.fixture
def hardware_provider():
    return Hardware()


def test_graphics(hardware_provider):
    graphics = hardware_provider.graphics()
    assert graphics in GRAPHICS
