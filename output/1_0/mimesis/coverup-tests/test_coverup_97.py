# file mimesis/providers/hardware.py:78-86
# lines [78, 86]
# branches []

import pytest
from mimesis.providers.hardware import Hardware

# Assuming GENERATION is a list of strings as the original code suggests
GENERATION = ["1st Generation", "2nd Generation", "3rd Generation"]

@pytest.fixture
def hardware_provider():
    return Hardware()

def test_hardware_generation(hardware_provider, mocker):
    # Since GENERATION is a list of strings, we can test all possible values
    for generation in GENERATION:
        # Patch the random.choice method to return the current generation
        mocker.patch('mimesis.random.Random.choice', return_value=generation)
        result = hardware_provider.generation()
        assert result == generation, f"Expected generation {generation} but got {result}"
