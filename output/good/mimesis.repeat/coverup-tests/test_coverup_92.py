# file mimesis/providers/internet.py:276-287
# lines [276, 285, 286, 287]
# branches []

import pytest
from mimesis.enums import Layer
from mimesis.providers.internet import Internet

# Assuming NETWORK_PROTOCOLS is a constant dictionary defined in the same module
# as the Internet class, we need to import it for our tests.
from mimesis.data import NETWORK_PROTOCOLS

@pytest.fixture
def internet_provider():
    return Internet()

def test_network_protocol_with_layer(internet_provider):
    for layer in Layer:
        protocol = internet_provider.network_protocol(layer=layer)
        assert protocol in NETWORK_PROTOCOLS[layer.value]

def test_network_protocol_without_layer(internet_provider):
    protocol = internet_provider.network_protocol()
    assert any(protocol in NETWORK_PROTOCOLS[layer.value] for layer in Layer)
