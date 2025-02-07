# file: tornado/httpclient.py:185-189
# asked: {"lines": [185, 186, 187, 189], "branches": []}
# gained: {"lines": [185, 186, 187, 189], "branches": []}

import pytest
from tornado.httpclient import AsyncHTTPClient
from tornado.simple_httpclient import SimpleAsyncHTTPClient

def test_configurable_default():
    default_client = AsyncHTTPClient.configurable_default()
    assert default_client is SimpleAsyncHTTPClient
