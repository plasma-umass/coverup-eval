# file httpie/client.py:135-144
# lines [135, 136, 139, 140, 141, 142, 144]
# branches []

import pytest
import http.client
from contextlib import contextmanager
from httpie.client import max_headers

def test_max_headers(mocker):
    # Mock the original _MAXHEADERS value
    original_max_headers = http.client._MAXHEADERS
    mocker.patch('http.client._MAXHEADERS', original_max_headers)

    new_limit = 100

    with max_headers(new_limit):
        assert http.client._MAXHEADERS == new_limit

    # Ensure the original value is restored
    assert http.client._MAXHEADERS == original_max_headers
