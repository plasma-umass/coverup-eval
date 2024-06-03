# file tornado/netutil.py:447-459
# lines [459]
# branches []

import pytest
from tornado.netutil import BlockingResolver

def test_blocking_resolver_initialize(mocker):
    # Mock the initialize method of the parent class ExecutorResolver
    mock_initialize = mocker.patch('tornado.netutil.ExecutorResolver.initialize')

    # Create an instance of BlockingResolver and call initialize
    resolver = BlockingResolver()
    
    # Ensure the initialize method is not called during instantiation
    mock_initialize.reset_mock()
    
    resolver.initialize()

    # Assert that the parent class's initialize method was called
    mock_initialize.assert_called_once()
