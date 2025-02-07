# file: httpie/utils.py:68-74
# asked: {"lines": [68, 69, 73, 74], "branches": []}
# gained: {"lines": [68, 69, 73, 74], "branches": []}

import pytest
import requests
from httpie.utils import ExplicitNullAuth

def test_explicit_null_auth():
    # Create an instance of ExplicitNullAuth
    auth = ExplicitNullAuth()
    
    # Create a mock request object
    request = requests.Request()
    
    # Call the auth instance with the mock request
    result = auth(request)
    
    # Assert that the result is the same as the request passed in
    assert result is request
