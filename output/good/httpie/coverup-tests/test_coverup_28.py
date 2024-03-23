# file httpie/client.py:300-324
# lines [300, 317, 318, 320, 321, 323, 324]
# branches []

import pytest
from httpie.client import ensure_path_as_is
from urllib.parse import urlparse, urlunparse

@pytest.fixture
def mock_urlparse(mocker):
    mocker.patch('httpie.client.urlparse', side_effect=urlparse)
    mocker.patch('httpie.client.urlunparse', side_effect=urlunparse)

def test_ensure_path_as_is(mock_urlparse):
    original_url = 'http://example.com/../path'
    prepped_url = 'http://example.com/?query=123'
    expected_url = 'http://example.com/../path?query=123'
    result = ensure_path_as_is(original_url, prepped_url)
    assert result == expected_url
