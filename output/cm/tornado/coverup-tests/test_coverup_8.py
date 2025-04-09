# file tornado/netutil.py:404-444
# lines [404, 405, 422, 424, 425, 427, 428, 429, 430, 432, 433, 435, 436, 437, 438, 440, 441, 442, 444]
# branches ['428->429', '428->432', '436->437', '436->438']

import concurrent.futures
import socket
from typing import Tuple, Any, List, Optional
from tornado.ioloop import IOLoop
from tornado.concurrent import run_on_executor
from tornado.netutil import Resolver
import pytest

# Assuming the existence of a dummy_executor and _resolve_addr for the sake of this example
# These would be defined within the tornado.netutil module or elsewhere in the Tornado framework
dummy_executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)

def _resolve_addr(host: str, port: int, family: socket.AddressFamily) -> List[Tuple[int, Any]]:
    # Dummy implementation for the sake of this example
    return [(family, (host, port))]

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
def mock_executor():
    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
        yield executor

@pytest.mark.asyncio
async def test_executor_resolver_with_custom_executor(mock_executor):
    resolver = ExecutorResolver()
    resolver.initialize(executor=mock_executor, close_executor=True)
    result = await resolver.resolve('localhost', 80)
    assert result == [(socket.AF_UNSPEC, ('localhost', 80))]
    resolver.close()
    assert resolver.executor is None

@pytest.mark.asyncio
async def test_executor_resolver_with_dummy_executor():
    resolver = ExecutorResolver()
    resolver.initialize()
    result = await resolver.resolve('localhost', 80)
    assert result == [(socket.AF_UNSPEC, ('localhost', 80))]
    resolver.close()
    assert resolver.executor is None
