# file tornado/netutil.py:404-444
# lines [404, 405, 422, 424, 425, 427, 428, 429, 430, 432, 433, 435, 436, 437, 438, 440, 441, 442, 444]
# branches ['428->429', '428->432', '436->437', '436->438']

import pytest
from unittest import mock
from tornado.ioloop import IOLoop
from tornado.netutil import Resolver
import concurrent.futures
import socket

class TestExecutorResolver:
    @pytest.fixture
    def resolver(self):
        from tornado.netutil import ExecutorResolver
        return ExecutorResolver()

    def test_initialize_with_executor(self, resolver):
        executor = concurrent.futures.ThreadPoolExecutor()
        resolver.initialize(executor=executor, close_executor=True)
        assert resolver.executor == executor
        assert resolver.close_executor is True

    def test_initialize_without_executor(self, resolver):
        resolver.initialize(executor=None, close_executor=True)
        assert resolver.executor is not None
        assert resolver.close_executor is False

    def test_close_with_executor(self, resolver):
        executor = concurrent.futures.ThreadPoolExecutor()
        resolver.initialize(executor=executor, close_executor=True)
        with mock.patch.object(executor, 'shutdown', wraps=executor.shutdown) as mock_shutdown:
            resolver.close()
            mock_shutdown.assert_called_once()
        assert resolver.executor is None

    def test_close_without_executor(self, resolver):
        resolver.initialize(executor=None, close_executor=False)
        resolver.close()
        assert resolver.executor is None

    @pytest.mark.asyncio
    async def test_resolve(self, resolver):
        resolver.initialize(executor=None, close_executor=False)
        result = await resolver.resolve('localhost', 80)
        assert isinstance(result, list)
        assert all(isinstance(item, tuple) for item in result)
