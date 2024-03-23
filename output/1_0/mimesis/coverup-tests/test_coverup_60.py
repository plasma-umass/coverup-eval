# file mimesis/providers/hardware.py:52-60
# lines [52, 60]
# branches []

import pytest
from mimesis.providers.hardware import Hardware

# Assuming the CPU constant is defined somewhere in the module
# If it's not, we'll need to mock it for the test
from mimesis.providers.hardware import CPU


@pytest.fixture
def hardware_provider():
    return Hardware()


def test_cpu(hardware_provider):
    cpu_name = hardware_provider.cpu()
    assert cpu_name in CPU
