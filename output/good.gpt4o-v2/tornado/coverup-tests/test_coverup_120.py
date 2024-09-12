# file: tornado/tcpclient.py:213-215
# asked: {"lines": [213, 214, 215], "branches": [[214, 0], [214, 215]]}
# gained: {"lines": [213, 214, 215], "branches": [[214, 0], [214, 215]]}

import pytest
from tornado.tcpclient import TCPClient
from tornado.netutil import Resolver

def test_tcpclient_close_with_own_resolver(mocker):
    resolver_mock = mocker.Mock(spec=Resolver)
    mocker.patch('tornado.tcpclient.Resolver', return_value=resolver_mock)
    
    client = TCPClient()
    client.close()
    
    resolver_mock.close.assert_called_once()

def test_tcpclient_close_without_own_resolver(mocker):
    resolver_mock = mocker.Mock(spec=Resolver)
    
    client = TCPClient(resolver=resolver_mock)
    client.close()
    
    resolver_mock.close.assert_not_called()
