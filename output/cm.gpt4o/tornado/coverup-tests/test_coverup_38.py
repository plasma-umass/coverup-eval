# file tornado/tcpclient.py:111-127
# lines [111, 112, 113, 114, 118, 119, 120, 122, 123, 124, 125, 126]
# branches ['118->119', '118->122']

import pytest
import socket
from unittest import mock
from tornado.tcpclient import TCPClient
from tornado.iostream import IOStream
from tornado.concurrent import Future
from typing import Iterator, Tuple
import functools

class TestTCPClient:
    @pytest.fixture
    def connector(self):
        class _Connector:
            def __init__(self):
                self.remaining = 0
                self.future = Future()
                self.last_error = None
                self.streams = set()

            def connect(self, af, addr):
                stream = mock.Mock(spec=IOStream)
                future = Future()
                future.set_result(None)
                return stream, future

            def on_connect_done(self, addrs, af, addr, future):
                pass

            def try_connect(self, addrs: Iterator[Tuple[socket.AddressFamily, Tuple]]) -> None:
                try:
                    af, addr = next(addrs)
                except StopIteration:
                    if self.remaining == 0 and not self.future.done():
                        self.future.set_exception(
                            self.last_error or IOError("connection failed")
                        )
                    return
                stream, future = self.connect(af, addr)
                self.streams.add(stream)
                future.add_done_callback(
                    functools.partial(self.on_connect_done, addrs, af, addr)
                )

        return _Connector()

    def test_try_connect_stop_iteration(self, connector):
        addrs = iter([])  # Empty iterator to trigger StopIteration
        connector.try_connect(addrs)
        assert connector.future.done()
        assert isinstance(connector.future.exception(), IOError)
        assert str(connector.future.exception()) == "connection failed"

    def test_try_connect_success(self, connector):
        addrs = iter([(socket.AF_INET, ('127.0.0.1', 80))])
        connector.try_connect(addrs)
        assert not connector.future.done()
        assert len(connector.streams) == 1
