# file tornado/netutil.py:447-459
# lines [459]
# branches []

import pytest
from tornado.netutil import BlockingResolver, ExecutorResolver

@pytest.fixture
def blocking_resolver():
    resolver = BlockingResolver()
    yield resolver
    # No specific cleanup required for BlockingResolver

def test_blocking_resolver_initialize(mocker):
    # Mock the superclass initialize method to confirm it's being called
    mock_super_init = mocker.patch.object(ExecutorResolver, 'initialize', return_value=None)
    
    resolver = BlockingResolver()
    resolver.initialize()
    
    # Check that the superclass initialize method was called
    assert mock_super_init.called
