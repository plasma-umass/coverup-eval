# file: tornado/httpclient.py:314-336
# asked: {"lines": [336], "branches": []}
# gained: {"lines": [336], "branches": []}

import pytest
from tornado.httpclient import AsyncHTTPClient
from tornado.simple_httpclient import SimpleAsyncHTTPClient
from tornado.util import Configurable

class CustomAsyncHTTPClient(AsyncHTTPClient):
    pass

def test_configure_with_class():
    # Test configuring with a class
    AsyncHTTPClient.configure(CustomAsyncHTTPClient)
    assert AsyncHTTPClient.configured_class() == CustomAsyncHTTPClient

def test_configure_with_class_name():
    # Test configuring with a class name
    AsyncHTTPClient.configure('tornado.httpclient.AsyncHTTPClient')
    assert AsyncHTTPClient.configured_class() == AsyncHTTPClient

def test_configure_with_none():
    # Test configuring with None
    AsyncHTTPClient.configure(None)
    assert AsyncHTTPClient.configured_class() == SimpleAsyncHTTPClient

@pytest.fixture(autouse=True)
def reset_configurable():
    # Reset the configuration after each test to avoid state pollution
    yield
    Configurable._impl_class = None
    Configurable._impl_kwargs = None
