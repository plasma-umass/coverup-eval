# file mimesis/providers/hardware.py:32-40
# lines [32, 40]
# branches []

import pytest
from mimesis.providers.hardware import Hardware

# Assuming RESOLUTIONS is a constant defined in the mimesis.providers.hardware module
# If it's not, you'll need to import or define it accordingly.

@pytest.fixture
def hardware_provider():
    return Hardware()

def test_resolution(hardware_provider):
    resolution = hardware_provider.resolution()
    # Assuming RESOLUTIONS is defined in the same module but not as a class attribute
    from mimesis.providers.hardware import RESOLUTIONS
    assert resolution in RESOLUTIONS
