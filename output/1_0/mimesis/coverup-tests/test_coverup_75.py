# file mimesis/providers/hardware.py:42-50
# lines [42, 50]
# branches []

import pytest
from mimesis.providers.hardware import Hardware

# Assuming SCREEN_SIZES is defined somewhere in the module
# If not, we need to define it for the purpose of this test
SCREEN_SIZES = ['13″', '15″', '17″']

# Mocking the Hardware class to include SCREEN_SIZES
@pytest.fixture
def hardware_provider(mocker):
    mocker.patch('mimesis.providers.hardware.SCREEN_SIZES', SCREEN_SIZES)
    return Hardware()

def test_screen_size(hardware_provider):
    screen_size = hardware_provider.screen_size()
    assert screen_size in SCREEN_SIZES
