# file: tornado/netutil.py:447-459
# asked: {"lines": [447, 448, 458, 459], "branches": []}
# gained: {"lines": [447, 448, 458, 459], "branches": []}

import pytest
from tornado.netutil import BlockingResolver
from tornado.ioloop import IOLoop

@pytest.fixture
def mock_executor_resolver(mocker):
    mocker.patch('tornado.netutil.ExecutorResolver.initialize')

def test_blocking_resolver_initialization(mock_executor_resolver):
    resolver = BlockingResolver()
    resolver.initialize()
    # No specific attributes to check, just ensure no exceptions are raised
    assert isinstance(resolver, BlockingResolver)

@pytest.fixture
def clean_ioloop():
    loop = IOLoop.current()
    yield loop
    loop.clear_current()
    loop.close(all_fds=True)

def test_blocking_resolver_with_ioloop(clean_ioloop, mock_executor_resolver):
    resolver = BlockingResolver()
    resolver.initialize()
    # No specific attributes to check, just ensure no exceptions are raised
    assert isinstance(resolver, BlockingResolver)
    assert IOLoop.current() is not None
