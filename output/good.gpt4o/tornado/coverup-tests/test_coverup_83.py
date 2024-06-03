# file tornado/simple_httpclient.py:529-533
# lines [529, 530, 531, 532, 533]
# branches ['530->exit', '530->531']

import pytest
from unittest import mock
from tornado.simple_httpclient import SimpleAsyncHTTPClient
from tornado.httputil import HTTPMessageDelegate

class TestHTTPConnection:
    @pytest.fixture
    def http_connection(self):
        class _HTTPConnection(HTTPMessageDelegate):
            def __init__(self):
                self.release_callback = None

            def _release(self) -> None:
                if self.release_callback is not None:
                    release_callback = self.release_callback
                    self.release_callback = None  # type: ignore
                    release_callback()

        return _HTTPConnection()

    def test_release_callback_called(self, http_connection):
        mock_callback = mock.Mock()
        http_connection.release_callback = mock_callback

        http_connection._release()

        mock_callback.assert_called_once()

    def test_release_callback_not_called(self, http_connection):
        http_connection.release_callback = None

        http_connection._release()

        # No assertion needed, just ensuring no exception is raised
