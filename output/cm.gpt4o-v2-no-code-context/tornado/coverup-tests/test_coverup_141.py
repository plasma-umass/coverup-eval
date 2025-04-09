# file: tornado/httpclient.py:112-113
# asked: {"lines": [112, 113], "branches": []}
# gained: {"lines": [112, 113], "branches": []}

import pytest
from tornado.httpclient import HTTPClient

def test_httpclient_del_method(mocker):
    mock_close = mocker.patch.object(HTTPClient, 'close')
    client = HTTPClient()
    del client
    mock_close.assert_called_once()
