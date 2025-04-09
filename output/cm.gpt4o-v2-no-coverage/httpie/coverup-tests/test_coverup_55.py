# file: httpie/utils.py:68-74
# asked: {"lines": [68, 69, 73, 74], "branches": []}
# gained: {"lines": [68, 69, 73, 74], "branches": []}

import pytest
import requests
from httpie.utils import ExplicitNullAuth

def test_explicit_null_auth_call():
    auth = ExplicitNullAuth()
    request = requests.Request('GET', 'http://example.com')
    prepared_request = request.prepare()
    
    # Call the auth instance with the prepared request
    result = auth(prepared_request)
    
    # Assert that the result is the same as the prepared request
    assert result is prepared_request
