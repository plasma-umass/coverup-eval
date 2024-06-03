# file tornado/netutil.py:365-371
# lines [365, 371]
# branches []

import pytest
from tornado.netutil import Resolver

def test_resolver_close(mocker):
    resolver = Resolver()
    close_spy = mocker.spy(resolver, 'close')
    
    resolver.close()
    
    close_spy.assert_called_once()
