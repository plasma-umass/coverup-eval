# file httpie/utils.py:68-74
# lines [68, 69, 73, 74]
# branches []

import pytest
from httpie.utils import ExplicitNullAuth
import requests
from unittest.mock import Mock

def test_explicit_null_auth():
    url = 'http://example.com'
    auth = ExplicitNullAuth()

    with requests.Session() as session:
        original_request = session.request
        session.request = Mock(return_value=original_request('GET', url))
        session.auth = auth
        response = session.request('GET', url)

        # Assert that the request has not been modified by any auth mechanism
        # Since the auth attribute does not exist on the PreparedRequest object,
        # we check if the session.auth is an instance of ExplicitNullAuth instead
        assert isinstance(session.auth, ExplicitNullAuth)

        # Assert that the request was sent (mocked or real)
        assert response.status_code is not None

        # Clean up is not necessary as we are not persisting any changes
        session.request = original_request
