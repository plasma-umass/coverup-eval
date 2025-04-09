# file tornado/simple_httpclient.py:542-576
# lines [542, 548, 549, 550, 551, 552, 554, 555, 556, 557, 558, 559, 560, 561, 565, 569, 570, 576]
# branches ['548->549', '548->576', '550->551', '550->555', '551->552', '551->554', '565->569', '565->570']

import pytest
from tornado.simple_httpclient import SimpleAsyncHTTPClient, HTTPStreamClosedError, HTTPResponse
from tornado.httpclient import HTTPRequest
from tornado.iostream import StreamClosedError
from unittest.mock import Mock
from types import TracebackType
from typing import Optional, Type


class TestHTTPConnection:
    @pytest.mark.gen_test
    async def test_handle_exception_with_final_callback(self, mocker):
        from tornado.simple_httpclient import _HTTPConnection

        # Mocking the necessary parts of _HTTPConnection
        conn = _HTTPConnection(Mock(), Mock(), Mock(), Mock(), Mock())
        conn.final_callback = Mock()
        conn._remove_timeout = Mock()
        conn._run_callback = Mock()
        conn.io_loop = Mock()
        conn.io_loop.time.return_value = 10
        conn.start_time = 5
        conn.start_wall_time = 1
        conn.stream = Mock()
        conn.stream.close = Mock()
        conn.request = HTTPRequest(url='http://example.com')

        # Mocking exception to be handled
        typ: "Optional[Type[BaseException]]" = StreamClosedError
        value: Optional[BaseException] = StreamClosedError()
        tb: Optional[TracebackType] = None

        # Call the method under test
        result = conn._handle_exception(typ, value, tb)

        # Assertions to verify postconditions
        conn._remove_timeout.assert_called_once()
        conn._run_callback.assert_called_once()
        conn.stream.close.assert_called_once()
        assert result is True

    @pytest.mark.gen_test
    async def test_handle_exception_without_final_callback(self, mocker):
        from tornado.simple_httpclient import _HTTPConnection

        # Mocking the necessary parts of _HTTPConnection
        conn = _HTTPConnection(Mock(), Mock(), Mock(), Mock(), Mock())
        conn.final_callback = None

        # Mocking exception to be handled
        typ: "Optional[Type[BaseException]]" = StreamClosedError
        value: Optional[BaseException] = StreamClosedError()
        tb: Optional[TracebackType] = None

        # Call the method under test
        result = conn._handle_exception(typ, value, tb)

        # Assertions to verify postconditions
        assert result is True

    @pytest.mark.gen_test
    async def test_handle_exception_with_non_streamclosederror(self, mocker):
        from tornado.simple_httpclient import _HTTPConnection

        # Mocking the necessary parts of _HTTPConnection
        conn = _HTTPConnection(Mock(), Mock(), Mock(), Mock(), Mock())
        conn.final_callback = None

        # Mocking exception to be handled
        typ: "Optional[Type[BaseException]]" = Exception
        value: Optional[BaseException] = Exception("Some error")
        tb: Optional[TracebackType] = None

        # Call the method under test
        result = conn._handle_exception(typ, value, tb)

        # Assertions to verify postconditions
        assert result is False
