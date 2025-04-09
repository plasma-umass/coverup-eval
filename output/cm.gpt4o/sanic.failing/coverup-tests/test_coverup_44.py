# file sanic/helpers.py:123-139
# lines [123, 133, 134, 135, 136, 137, 139]
# branches []

import pytest
from sanic.helpers import remove_entity_headers

def is_entity_header(header):
    # Mock implementation of is_entity_header for testing purposes
    entity_headers = {
        "content-type", "content-length", "content-language", "content-encoding",
        "content-location", "expires", "last-modified", "etag"
    }
    return header.lower() in entity_headers

@pytest.fixture
def mock_is_entity_header(mocker):
    return mocker.patch('sanic.helpers.is_entity_header', side_effect=is_entity_header)

def test_remove_entity_headers(mock_is_entity_header):
    headers = {
        "Content-Type": "text/html",
        "Content-Length": "1234",
        "Content-Language": "en",
        "Content-Encoding": "gzip",
        "Content-Location": "http://example.com",
        "Expires": "Wed, 21 Oct 2015 07:28:00 GMT",
        "Last-Modified": "Wed, 21 Oct 2015 07:28:00 GMT",
        "ETag": "abc123",
        "Custom-Header": "custom_value"
    }

    expected_headers = {
        "Content-Location": "http://example.com",
        "Expires": "Wed, 21 Oct 2015 07:28:00 GMT",
        "Custom-Header": "custom_value"
    }

    result = remove_entity_headers(headers)
    assert result == expected_headers

    # Test with different allowed headers
    allowed = ("content-location", "expires", "etag")
    expected_headers_with_etag = {
        "Content-Location": "http://example.com",
        "Expires": "Wed, 21 Oct 2015 07:28:00 GMT",
        "ETag": "abc123",
        "Custom-Header": "custom_value"
    }

    result_with_etag = remove_entity_headers(headers, allowed)
    assert result_with_etag == expected_headers_with_etag
