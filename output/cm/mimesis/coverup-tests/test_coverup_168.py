# file mimesis/providers/internet.py:276-287
# lines [285, 286, 287]
# branches []

import pytest
from mimesis.enums import Layer
from mimesis.providers.internet import Internet

# Assuming NETWORK_PROTOCOLS is a constant defined in the same module as the Internet class
from mimesis.providers.internet import NETWORK_PROTOCOLS

@pytest.fixture
def internet_provider():
    return Internet()

def test_network_protocol_with_layer(internet_provider):
    for layer in Layer:
        protocol = internet_provider.network_protocol(layer=layer)
        assert protocol in NETWORK_PROTOCOLS[layer.value]

def test_network_protocol_without_layer(internet_provider):
    protocol = internet_provider.network_protocol()
    assert any(protocol in protocols for protocols in NETWORK_PROTOCOLS.values())
