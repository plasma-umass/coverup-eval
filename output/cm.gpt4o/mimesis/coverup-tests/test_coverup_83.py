# file mimesis/providers/internet.py:276-287
# lines [276, 285, 286, 287]
# branches []

import pytest
from mimesis.providers.internet import Internet
from mimesis.enums import Layer
from unittest.mock import patch

NETWORK_PROTOCOLS = {
    Layer.APPLICATION: ['HTTP', 'FTP', 'SMTP'],
    Layer.PRESENTATION: ['TLS', 'SSL'],
    Layer.SESSION: ['NetBIOS', 'RPC'],
    Layer.TRANSPORT: ['TCP', 'UDP'],
    Layer.NETWORK: ['IP', 'ICMP'],
    Layer.DATA_LINK: ['Ethernet', 'PPP'],
    Layer.PHYSICAL: ['DSL', 'ISDN'],
}

@pytest.fixture
def internet():
    return Internet()

def test_network_protocol_with_layer(internet):
    with patch('mimesis.providers.internet.Internet._validate_enum', return_value=Layer.APPLICATION) as mock_validate_enum:
        with patch('mimesis.providers.internet.NETWORK_PROTOCOLS', NETWORK_PROTOCOLS):
            protocol = internet.network_protocol(Layer.APPLICATION)
            assert protocol in NETWORK_PROTOCOLS[Layer.APPLICATION]
            mock_validate_enum.assert_called_once_with(item=Layer.APPLICATION, enum=Layer)

def test_network_protocol_without_layer(internet):
    with patch('mimesis.providers.internet.Internet._validate_enum', return_value=Layer.APPLICATION) as mock_validate_enum:
        with patch('mimesis.providers.internet.NETWORK_PROTOCOLS', NETWORK_PROTOCOLS):
            protocol = internet.network_protocol()
            assert protocol in NETWORK_PROTOCOLS[Layer.APPLICATION]
            mock_validate_enum.assert_called_once_with(item=None, enum=Layer)
