# file: tornado/netutil.py:365-371
# asked: {"lines": [365, 371], "branches": []}
# gained: {"lines": [365, 371], "branches": []}

import pytest
from tornado.netutil import Resolver

def test_resolver_close():
    resolver = Resolver()
    resolver.close()
    # No specific postconditions to assert for close method as it is a no-op.
