# file: tornado/netutil.py:365-371
# asked: {"lines": [365, 371], "branches": []}
# gained: {"lines": [365, 371], "branches": []}

import pytest
from tornado.netutil import Resolver

def test_resolver_close():
    resolver = Resolver()
    resolver.close()
    # Since the close method does nothing, we just ensure it can be called without error.
    assert resolver is not None
