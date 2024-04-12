# file tornado/netutil.py:331-333
# lines [331, 332, 333]
# branches []

import pytest
from tornado.netutil import Resolver

def test_resolver_configurable_base():
    # Test that the configurable_base method returns the Resolver class itself
    assert Resolver.configurable_base() is Resolver

    # Cleanup is not necessary for this test as we are not creating any external resources
