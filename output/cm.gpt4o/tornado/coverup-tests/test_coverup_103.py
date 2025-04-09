# file tornado/httpclient.py:181-183
# lines [181, 182, 183]
# branches []

import pytest
from tornado.httpclient import AsyncHTTPClient

def test_configurable_base():
    # Verify that the configurable_base method returns AsyncHTTPClient
    assert AsyncHTTPClient.configurable_base() is AsyncHTTPClient
