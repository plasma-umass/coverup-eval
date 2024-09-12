# file: tornado/netutil.py:447-459
# asked: {"lines": [447, 448, 458, 459], "branches": []}
# gained: {"lines": [447, 448, 458, 459], "branches": []}

import pytest
from tornado.netutil import BlockingResolver
from tornado.ioloop import IOLoop

@pytest.fixture
def resolver():
    return BlockingResolver()

def test_blocking_resolver_initialize(resolver):
    resolver.initialize()
    assert isinstance(resolver, BlockingResolver)

def test_blocking_resolver_deprecated_warning():
    with pytest.deprecated_call():
        resolver = BlockingResolver()
        resolver.initialize()
