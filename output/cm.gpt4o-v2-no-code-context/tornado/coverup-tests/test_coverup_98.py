# file: tornado/httpclient.py:181-183
# asked: {"lines": [181, 182, 183], "branches": []}
# gained: {"lines": [181, 182, 183], "branches": []}

import pytest
from tornado.httpclient import AsyncHTTPClient
from tornado.util import Configurable

def test_configurable_base():
    assert AsyncHTTPClient.configurable_base() == AsyncHTTPClient

@pytest.fixture(autouse=True)
def cleanup():
    yield
    # Add any necessary cleanup code here
