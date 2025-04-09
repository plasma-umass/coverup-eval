# file: tornado/netutil.py:331-333
# asked: {"lines": [331, 332, 333], "branches": []}
# gained: {"lines": [331, 332, 333], "branches": []}

import pytest
from tornado.netutil import Resolver

def test_configurable_base():
    assert Resolver.configurable_base() is Resolver
