# file tornado/tcpclient.py:75-98
# lines [75, 76, 90, 91, 92, 93, 94, 95, 97, 98]
# branches ['93->94', '93->98', '94->95', '94->97']

import socket
import pytest
from tornado.tcpclient import _Connector

@pytest.fixture
def mock_addrinfo():
    # Mock addrinfo with mixed address families
    return [
        (socket.AF_INET, ('127.0.0.1', 80)),
        (socket.AF_INET6, ('::1', 80)),
        (socket.AF_INET, ('192.168.1.1', 80)),
        (socket.AF_INET6, ('fe80::1', 80)),
    ]

def test_connector_split(mock_addrinfo):
    primary, secondary = _Connector.split(mock_addrinfo)
    
    # Assertions to check if the primary list contains only the first address family
    assert all(af == mock_addrinfo[0][0] for af, _ in primary)
    # Assertions to check if the secondary list contains all other address families
    assert all(af != mock_addrinfo[0][0] for af, _ in secondary)
    # Assertions to check if all addresses are accounted for
    assert len(primary) + len(secondary) == len(mock_addrinfo)
    # Assertions to check if the first address is in the primary list
    assert mock_addrinfo[0] in primary
    # Assertions to check if the second address is in the secondary list
    assert mock_addrinfo[1] in secondary
