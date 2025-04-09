# file: httpie/utils.py:68-74
# asked: {"lines": [68, 69, 73, 74], "branches": []}
# gained: {"lines": [68, 69, 73, 74], "branches": []}

import pytest
import requests
from httpie.utils import ExplicitNullAuth

def test_explicit_null_auth(monkeypatch):
    # Create a mock request object
    class MockRequest:
        def __init__(self):
            self.headers = {}

    mock_request = MockRequest()

    # Instantiate the ExplicitNullAuth class
    auth = ExplicitNullAuth()

    # Call the auth instance with the mock request
    result = auth(mock_request)

    # Assert that the result is the same as the mock request
    assert result is mock_request

    # Clean up any state if necessary (not needed in this case)
