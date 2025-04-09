# file tornado/httpclient.py:185-189
# lines [185, 186, 187, 189]
# branches []

import pytest
from tornado.httpclient import AsyncHTTPClient
from tornado.simple_httpclient import SimpleAsyncHTTPClient

def test_configurable_default():
    default_client = AsyncHTTPClient.configurable_default()
    assert default_client is SimpleAsyncHTTPClient, "The default configurable should be SimpleAsyncHTTPClient"
