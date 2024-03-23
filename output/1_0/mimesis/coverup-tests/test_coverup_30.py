# file mimesis/providers/hardware.py:27-30
# lines [27, 28, 30]
# branches []

import pytest
from mimesis.providers.hardware import Hardware

def test_hardware_meta():
    hardware = Hardware()
    assert hardware.Meta.name == 'hardware'
