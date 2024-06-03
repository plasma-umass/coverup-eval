# file sanic/helpers.py:123-139
# lines [123, 133, 134, 135, 136, 137, 139]
# branches []

import pytest
from sanic.helpers import remove_entity_headers

def is_entity_header(header):
    # Mock implementation of is_entity_header for testing purposes
    entity_headers = {
        "allow", "content-encoding", "content-language", "content-length",
        "content-location", "content-md5", "content-range", "content-type",
        "expires", "last-modified"
    }
    return header.lower() in entity_headers

def test_remove_entity_headers():
    headers = {
        "Content-Type": "text/html",
        "Content-Length": "1234",
        "Content-Location": "http://example.com",
        "Expires": "Wed, 21 Oct 2015 07:28:00 GMT",
        "Cache-Control": "no-cache",
        "X-Custom-Header": "custom_value"
    }
    
    expected_headers = {
        "Content-Location": "http://example.com",
        "Expires": "Wed, 21 Oct 2015 07:28:00 GMT",
        "Cache-Control": "no-cache",
        "X-Custom-Header": "custom_value"
    }
    
    result = remove_entity_headers(headers)
    assert result == expected_headers

    # Test with different allowed headers
    result = remove_entity_headers(headers, allowed=("content-type", "cache-control"))
    expected_headers = {
        "Content-Type": "text/html",
        "Cache-Control": "no-cache",
        "X-Custom-Header": "custom_value"
    }
    assert result == expected_headers

    # Test with no allowed headers
    result = remove_entity_headers(headers, allowed=())
    expected_headers = {
        "Cache-Control": "no-cache",
        "X-Custom-Header": "custom_value"
    }
    assert result == expected_headers

    # Test with all headers allowed
    result = remove_entity_headers(headers, allowed=headers.keys())
    assert result == headers

@pytest.fixture(autouse=True)
def mock_is_entity_header(mocker):
    mocker.patch('sanic.helpers.is_entity_header', side_effect=is_entity_header)
