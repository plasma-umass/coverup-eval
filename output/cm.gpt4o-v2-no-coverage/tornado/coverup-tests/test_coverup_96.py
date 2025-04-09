# file: tornado/netutil.py:447-459
# asked: {"lines": [447, 448, 458, 459], "branches": []}
# gained: {"lines": [447, 448, 458, 459], "branches": []}

import pytest
from tornado.netutil import BlockingResolver
from tornado.concurrent import dummy_executor
from tornado.ioloop import IOLoop

class TestBlockingResolver:
    @pytest.fixture
    def resolver(self):
        return BlockingResolver()

    def test_initialize(self, resolver):
        resolver.initialize()
        assert resolver.io_loop == IOLoop.current()
        assert resolver.executor == dummy_executor
        assert resolver.close_executor is False
