# file sanic/helpers.py:118-120
# lines [118, 120]
# branches []

import pytest
from sanic.helpers import is_hop_by_hop_header

# Assuming _HOP_BY_HOP_HEADERS is defined somewhere in the sanic.helpers module
# If it's not publicly accessible, we might need to mock or infer its value
# For the purpose of this example, let's define it here as it would be in the module
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

@pytest.fixture
def cleanup():
    # Fixture for any required cleanup, add cleanup code if necessary
    yield
    # Cleanup code goes here

def test_is_hop_by_hop_header(cleanup):
    # Test with a known hop-by-hop header
    assert is_hop_by_hop_header("Connection") is True
    assert is_hop_by_hop_header("connection") is True

    # Test with a header that is not hop-by-hop
    assert is_hop_by_hop_header("Content-Type") is False

    # Test with a mixed case header that is hop-by-hop
    assert is_hop_by_hop_header("KeEp-AlIvE") is True

    # Test with a mixed case header that is not hop-by-hop
    assert is_hop_by_hop_header("Content-Length") is False
