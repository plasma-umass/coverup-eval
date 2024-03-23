# file mimesis/providers/hardware.py:125-133
# lines [125, 133]
# branches []

import pytest
from mimesis.providers.hardware import Hardware

# Assuming HDD_SSD is a list of strings like ["128GB SSD", "256GB SSD", "512GB HDD", "1TB HDD"]
# If HDD_SSD is not defined, we need to mock it for the test
HDD_SSD = ["128GB SSD", "256GB SSD", "512GB HDD", "1TB HDD"]

@pytest.fixture
def hardware_provider(mocker):
    mocker.patch('mimesis.providers.hardware.HDD_SSD', HDD_SSD)
    return Hardware()

def test_ssd_or_hdd(hardware_provider):
    result = hardware_provider.ssd_or_hdd()
    assert result in HDD_SSD
