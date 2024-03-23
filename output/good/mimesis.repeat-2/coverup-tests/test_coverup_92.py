# file mimesis/providers/internet.py:276-287
# lines [276, 285, 286, 287]
# branches []

import pytest
from mimesis.enums import Layer
from mimesis.providers.internet import Internet

@pytest.fixture
def internet_provider():
    return Internet()

def test_network_protocol_with_layer(internet_provider):
    for layer in Layer:
        protocol = internet_provider.network_protocol(layer=layer)
        # Assuming NETWORK_PROTOCOLS is a dictionary in the global scope of the module
        # We need to import it to access it
        from mimesis.providers.internet import NETWORK_PROTOCOLS
        assert protocol in NETWORK_PROTOCOLS[layer.value]

def test_network_protocol_without_layer(internet_provider):
    # Assuming NETWORK_PROTOCOLS is a dictionary in the global scope of the module
    # We need to import it to access it
    from mimesis.providers.internet import NETWORK_PROTOCOLS
    protocol = internet_provider.network_protocol()
    assert any(protocol in protocols for protocols in NETWORK_PROTOCOLS.values())
