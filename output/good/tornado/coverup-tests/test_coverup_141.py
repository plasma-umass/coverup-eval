# file tornado/simple_httpclient.py:255-259
# lines [255, 256, 257]
# branches []

import pytest
from tornado import simple_httpclient, httputil

# Assuming the code snippet provided is part of the simple_httpclient.py file
# and that the _HTTPConnection class has more content that is not shown here.

# The test will need to instantiate the _HTTPConnection class and check if the
# _SUPPORTED_METHODS attribute contains the correct set of HTTP methods.

@pytest.fixture
def http_connection():
    # Mocking the necessary parts of the _HTTPConnection class
    class MockHTTPConnection(simple_httpclient._HTTPConnection):
        def __init__(self, *args, **kwargs):
            pass  # Override the constructor to avoid side effects

    return MockHTTPConnection()

def test_supported_methods(http_connection):
    expected_methods = {"GET", "HEAD", "POST", "PUT", "DELETE", "PATCH", "OPTIONS"}
    assert http_connection._SUPPORTED_METHODS == expected_methods, "Supported methods do not match expected methods"
