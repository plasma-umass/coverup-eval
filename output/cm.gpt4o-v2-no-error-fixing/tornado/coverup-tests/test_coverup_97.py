# file: tornado/netutil.py:331-333
# asked: {"lines": [331, 332, 333], "branches": []}
# gained: {"lines": [331, 332, 333], "branches": []}

import pytest
from tornado.netutil import Resolver

def test_resolver_configurable_base():
    # Ensure that the configurable_base method returns the Resolver class
    assert Resolver.configurable_base() is Resolver
