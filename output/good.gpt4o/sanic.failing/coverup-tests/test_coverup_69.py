# file sanic/helpers.py:118-120
# lines [118, 120]
# branches []

import pytest
from sanic.helpers import is_hop_by_hop_header

def test_is_hop_by_hop_header():
    # Define the _HOP_BY_HOP_HEADERS for the test
    global _HOP_BY_HOP_HEADERS
    _HOP_BY_HOP_HEADERS = {
        'connection',
        'keep-alive',
        'proxy-authenticate',
        'proxy-authorization',
        'te',
        'trailers',
        'transfer-encoding',
        'upgrade'
    }

    # Test cases for headers that are hop-by-hop
    hop_by_hop_headers = [
        'Connection',
        'Keep-Alive',
        'Proxy-Authenticate',
        'Proxy-Authorization',
        'TE',
        'Trailers',
        'Transfer-Encoding',
        'Upgrade'
    ]

    for header in hop_by_hop_headers:
        assert is_hop_by_hop_header(header) is True

    # Test cases for headers that are not hop-by-hop
    non_hop_by_hop_headers = [
        'Content-Length',
        'Content-Type',
        'Date',
        'Server'
    ]

    for header in non_hop_by_hop_headers:
        assert is_hop_by_hop_header(header) is False

    # Clean up the global variable to avoid affecting other tests
    del _HOP_BY_HOP_HEADERS
