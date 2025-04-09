# file tornado/netutil.py:331-333
# lines [331, 332, 333]
# branches []

import pytest
from tornado.netutil import Resolver

def test_resolver_configurable_base():
    class TestResolver(Resolver):
        pass

    assert TestResolver.configurable_base() is Resolver
