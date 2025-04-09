# file mimesis/providers/internet.py:101-118
# lines [112, 114, 115, 116, 118]
# branches ['114->115', '114->118']

import pytest
from mimesis.providers.internet import Internet, PortRange

@pytest.fixture
def internet():
    return Internet()

def test_ip_v4_with_port(internet, mocker):
    mock_ip = "192.168.1.1"
    mock_port = 8080

    mocker.patch.object(internet, 'ip_v4_object', return_value=mock_ip)
    mocker.patch.object(internet, 'port', return_value=mock_port)

    result = internet.ip_v4(with_port=True, port_range=PortRange.ALL)
    assert result == f"{mock_ip}:{mock_port}"

def test_ip_v4_without_port(internet, mocker):
    mock_ip = "192.168.1.1"

    mocker.patch.object(internet, 'ip_v4_object', return_value=mock_ip)

    result = internet.ip_v4(with_port=False)
    assert result == mock_ip
