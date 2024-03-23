# file tornado/netutil.py:365-371
# lines [365, 371]
# branches []

import pytest
from tornado.netutil import Resolver

@pytest.fixture
def resolver():
    return Resolver()

def test_resolver_close(resolver):
    # Ensure that the close method can be called without errors
    try:
        resolver.close()
    except Exception as e:
        pytest.fail(f"Unexpected exception raised: {e}")
    # No postconditions to assert since the method is a no-op pass
