# file mimesis/providers/hardware.py:155-163
# lines [155, 163]
# branches []

import pytest
from mimesis.providers.hardware import Hardware
from mimesis.data import PHONE_MODELS

@pytest.fixture
def hardware_provider():
    return Hardware()

def test_phone_model(hardware_provider):
    phone_model = hardware_provider.phone_model()
    assert phone_model in PHONE_MODELS
