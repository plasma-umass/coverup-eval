# file: tornado/netutil.py:404-444
# asked: {"lines": [404, 405, 422, 424, 425, 427, 428, 429, 430, 432, 433, 435, 436, 437, 438, 440, 441, 442, 444], "branches": [[428, 429], [428, 432], [436, 437], [436, 438]]}
# gained: {"lines": [404, 405, 422, 424, 425, 435, 440, 441, 442], "branches": []}

import pytest
from unittest import mock
from tornado.ioloop import IOLoop
from tornado.concurrent import run_on_executor
from tornado.netutil import Resolver
import concurrent.futures
import socket
from typing import Optional, List, Tuple, Any

# Mocking the _resolve_addr function
def _resolve_addr(host: str, port: int, family: socket.AddressFamily) -> List[Tuple[int, Any]]:
    return [(socket.AF_INET, (host, port))]

# Dummy executor for testing
class DummyExecutor:
    def submit(self, fn, *args, **kwargs):
        return fn(*args, **kwargs)
    
    def shutdown(self):
        pass

dummy_executor = DummyExecutor()

class ExecutorResolver(Resolver):
    def initialize(
        self,
        executor: Optional[concurrent.futures.Executor] = None,
        close_executor: bool = True,
    ) -> None:
        self.io_loop = IOLoop.current()
        if executor is not None:
            self.executor = executor
            self.close_executor = close_executor
        else:
            self.executor = dummy_executor
            self.close_executor = False

    def close(self) -> None:
        if self.close_executor:
            self.executor.shutdown()
        self.executor = None  # type: ignore

    @run_on_executor
    def resolve(
        self, host: str, port: int, family: socket.AddressFamily = socket.AF_UNSPEC
    ) -> List[Tuple[int, Any]]:
        return _resolve_addr(host, port, family)

@pytest.fixture
def mock_ioloop(mocker):
    mock_ioloop = mocker.patch('tornado.ioloop.IOLoop.current', return_value=mock.Mock())
    return mock_ioloop

def test_initialize_with_executor(mock_ioloop):
    executor = concurrent.futures.ThreadPoolExecutor()
    resolver = ExecutorResolver()
    resolver.initialize(executor=executor, close_executor=True)
    
    assert resolver.executor == executor
    assert resolver.close_executor is True
    assert resolver.io_loop == mock_ioloop()

def test_initialize_without_executor(mock_ioloop):
    resolver = ExecutorResolver()
    resolver.initialize()
    
    assert resolver.executor == dummy_executor
    assert resolver.close_executor is False
    assert resolver.io_loop == mock_ioloop()

def test_close_with_executor(mock_ioloop):
    executor = mock.Mock()
    resolver = ExecutorResolver()
    resolver.initialize(executor=executor, close_executor=True)
    resolver.close()
    
    executor.shutdown.assert_called_once()
    assert resolver.executor is None

def test_close_without_executor(mock_ioloop):
    resolver = ExecutorResolver()
    resolver.initialize()
    resolver.close()
    
    assert resolver.executor is None

@pytest.mark.asyncio
async def test_resolve_with_executor(mock_ioloop):
    executor = concurrent.futures.ThreadPoolExecutor()
    resolver = ExecutorResolver()
    resolver.initialize(executor=executor, close_executor=True)
    
    result = await resolver.resolve('localhost', 80)
    assert result == [(socket.AF_INET, ('localhost', 80))]
    resolver.close()

@pytest.mark.asyncio
async def test_resolve_without_executor(mock_ioloop):
    resolver = ExecutorResolver()
    resolver.initialize()
    
    result = await resolver.resolve('localhost', 80)
    assert result == [(socket.AF_INET, ('localhost', 80))]
    resolver.close()
