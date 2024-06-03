# file sanic/helpers.py:118-120
# lines [118, 120]
# branches []

import pytest
from sanic.helpers import is_hop_by_hop_header

_HOP_BY_HOP_HEADERS = {
    "connection",
    "keep-alive",
    "proxy-authenticate",
    "proxy-authorization",
    "te",
    "trailer",
    "transfer-encoding",
    "upgrade",
}

def test_is_hop_by_hop_header():
    # Test with a header that is in the hop-by-hop headers list
    assert is_hop_by_hop_header("Connection") is True
    assert is_hop_by_hop_header("connection") is True
    assert is_hop_by_hop_header("keep-alive") is True
    assert is_hop_by_hop_header("Keep-Alive") is True

    # Test with a header that is not in the hop-by-hop headers list
    assert is_hop_by_hop_header("Content-Length") is False
    assert is_hop_by_hop_header("content-length") is False

    # Test with a header that is similar but not exactly in the list
    assert is_hop_by_hop_header("Connection-Upgrade") is False

    # Test with an empty string
    assert is_hop_by_hop_header("") is False

    # Test with a None value
    with pytest.raises(AttributeError):
        is_hop_by_hop_header(None)
