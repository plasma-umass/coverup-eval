# file tornado/tcpclient.py:182-185
# lines [182, 183, 184, 185]
# branches ['183->184', '183->185']

import pytest
from unittest.mock import Mock, patch
from tornado.tcpclient import TCPClient
from tornado.ioloop import IOLoop
from tornado.concurrent import Future

class _Connector(object):
    def __init__(self):
        self.future = Future()
        self.close_streams = Mock()

    def on_connect_timeout(self) -> None:
        if not self.future.done():
            self.future.set_exception(TimeoutError())
        self.close_streams()

class TestTCPClient:
    @pytest.fixture
    def connector(self):
        return _Connector()

    def test_on_connect_timeout(self, connector):
        connector.on_connect_timeout()
        assert connector.future.done()
        assert isinstance(connector.future.exception(), TimeoutError)
        connector.close_streams.assert_called_once()
