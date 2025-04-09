# file: tornado/netutil.py:447-459
# asked: {"lines": [459], "branches": []}
# gained: {"lines": [459], "branches": []}

import pytest
from tornado.netutil import BlockingResolver
from tornado.ioloop import IOLoop
from unittest.mock import patch, MagicMock

@pytest.fixture
def mock_ioloop_current(monkeypatch):
    mock_ioloop = MagicMock(spec=IOLoop)
    monkeypatch.setattr(IOLoop, 'current', lambda: mock_ioloop)
    return mock_ioloop

def test_blocking_resolver_initialize(mock_ioloop_current):
    resolver = BlockingResolver()
    with patch.object(BlockingResolver, 'initialize', wraps=resolver.initialize) as mock_initialize:
        resolver.initialize()
        mock_initialize.assert_called_once()
        assert resolver.io_loop == mock_ioloop_current
        assert resolver.executor is not None
        assert resolver.close_executor is False
