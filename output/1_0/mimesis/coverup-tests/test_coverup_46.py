# file mimesis/providers/transport.py:36-49
# lines [36, 46, 47, 48]
# branches []

import pytest
from mimesis.providers.transport import Transport
from mimesis.providers.base import BaseProvider

# Mock data for trucks
TRUCKS = ['Ford', 'Volvo', 'Freightliner']

# Mock class to replace the original Transport class for testing
class MockTransport(Transport):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.random = self._setup_mock_random()

    def _setup_mock_random(self):
        class MockRandom:
            @staticmethod
            def choice(seq):
                # Always return the first element for predictability
                return seq[0]

            def custom_code(self, mask):
                # Replace '@' with 'A' and '#' with '1' for predictability
                return mask.replace('@', 'A').replace('#', '1')

        return MockRandom()

@pytest.fixture
def mock_transport(mocker):
    mocker.patch('mimesis.providers.transport.TRUCKS', TRUCKS)
    return MockTransport()

def test_truck_model(mock_transport):
    expected_model = 'Ford-1111 AA'
    model = mock_transport.truck()
    assert model == expected_model, f"Expected truck model to be {expected_model}, but got {model}"
