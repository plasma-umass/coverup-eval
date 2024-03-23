# file mimesis/providers/transport.py:51-59
# lines [51, 59]
# branches []

import pytest
from mimesis.providers.transport import Transport

# Assuming the MANUFACTURERS constant is defined in the same module as the Transport class
# If it's not, you would need to import it from the correct location
from mimesis.providers.transport import MANUFACTURERS

@pytest.fixture
def transport_provider():
    return Transport()

def test_manufacturer(transport_provider):
    manufacturer = transport_provider.manufacturer()
    assert manufacturer in MANUFACTURERS
