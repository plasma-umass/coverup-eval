# file mimesis/providers/transport.py:31-34
# lines [31, 32, 34]
# branches []

import pytest
from mimesis.providers.transport import Transport
from mimesis import Generic

@pytest.fixture
def transport_provider():
    return Transport()

def test_transport_meta(transport_provider):
    assert transport_provider.Meta.name == 'transport'
