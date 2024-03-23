# file mimesis/providers/hardware.py:88-93
# lines [93]
# branches []

import pytest
from mimesis.providers.hardware import Hardware
from unittest.mock import patch

# Assuming CPU_MODEL_CODES is a constant list defined in the same module
# If it's defined elsewhere, you would need to import it accordingly
from mimesis.providers.hardware import CPU_MODEL_CODES

@pytest.fixture
def hardware_provider():
    return Hardware()

def test_cpu_model_code(hardware_provider):
    # Mock the random.choice method to ensure line 93 is executed
    with patch('mimesis.random.Random.choice') as mock_choice:
        mock_choice.return_value = 'mocked_cpu_code'
        cpu_code = hardware_provider.cpu_model_code()
        mock_choice.assert_called_once_with(CPU_MODEL_CODES)
        assert cpu_code == 'mocked_cpu_code'
