# file: tornado/httpclient.py:112-113
# asked: {"lines": [112, 113], "branches": []}
# gained: {"lines": [112, 113], "branches": []}

import pytest
from unittest import mock
from tornado.httpclient import HTTPClient

class TestHTTPClient:
    @mock.patch.object(HTTPClient, 'close', autospec=True)
    def test_del_method(self, mock_close):
        client = HTTPClient()
        del client
        mock_close.assert_called_once()
