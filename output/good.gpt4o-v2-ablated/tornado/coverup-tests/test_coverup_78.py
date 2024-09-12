# file: tornado/netutil.py:335-337
# asked: {"lines": [335, 336, 337], "branches": []}
# gained: {"lines": [335, 336, 337], "branches": []}

import pytest
from tornado.netutil import Resolver, DefaultExecutorResolver

def test_resolver_configurable_default():
    assert Resolver.configurable_default() is DefaultExecutorResolver
