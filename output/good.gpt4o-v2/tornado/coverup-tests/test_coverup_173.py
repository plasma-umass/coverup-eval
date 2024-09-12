# file: tornado/simple_httpclient.py:202-203
# asked: {"lines": [202, 203], "branches": []}
# gained: {"lines": [202, 203], "branches": []}

import pytest
from tornado.simple_httpclient import SimpleAsyncHTTPClient
from tornado.httpclient import HTTPRequest
from unittest.mock import patch

def test_connection_class():
    client = SimpleAsyncHTTPClient()
    with patch('tornado.simple_httpclient._HTTPConnection') as mock_connection:
        connection_class = client._connection_class()
        assert connection_class == mock_connection
