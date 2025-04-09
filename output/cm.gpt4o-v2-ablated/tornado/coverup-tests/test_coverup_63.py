# file: tornado/netutil.py:447-459
# asked: {"lines": [447, 448, 458, 459], "branches": []}
# gained: {"lines": [447, 448, 458, 459], "branches": []}

import pytest
from tornado.netutil import BlockingResolver
from tornado.ioloop import IOLoop

@pytest.fixture
def resolver():
    return BlockingResolver()

def test_blocking_resolver_initialize(mocker, resolver):
    mock_super_initialize = mocker.patch.object(BlockingResolver, 'initialize', autospec=True)
    resolver.initialize()
    mock_super_initialize.assert_called_once_with(resolver)
