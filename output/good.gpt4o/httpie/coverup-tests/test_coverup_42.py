# file httpie/utils.py:68-74
# lines [68, 69, 73, 74]
# branches []

import pytest
import requests
from httpie.utils import ExplicitNullAuth

def test_explicit_null_auth(mocker):
    # Mock a request object
    mock_request = mocker.Mock(spec=requests.PreparedRequest)
    
    # Create an instance of ExplicitNullAuth
    auth = ExplicitNullAuth()
    
    # Call the auth instance with the mock request
    result = auth(mock_request)
    
    # Assert that the result is the same as the mock request
    assert result is mock_request
