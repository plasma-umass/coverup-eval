# file sanic/helpers.py:123-139
# lines [123, 133, 134, 135, 136, 137, 139]
# branches []

import pytest
from sanic.helpers import remove_entity_headers

# Assuming `is_entity_header` is a function that needs to be mocked
# to control which headers are considered entity headers.
@pytest.fixture
def mock_is_entity_header(mocker):
    return mocker.patch('sanic.helpers.is_entity_header', return_value=False)

def test_remove_entity_headers_with_allowed(mock_is_entity_header):
    # Setup: Define headers with a mix of allowed and disallowed entity headers
    headers = {
        'Content-Type': 'text/html',
        'Content-Length': '123',
        'Content-Location': 'http://example.com',
        'Expires': 'Wed, 21 Oct 2021 07:28:00 GMT',
        'Last-Modified': 'Wed, 21 Oct 2020 07:28:00 GMT'
    }
    # Mock `is_entity_header` to return True for specific headers
    mock_is_entity_header.side_effect = lambda h: h.lower() in ['content-length', 'last-modified']

    # Execute: Call the function under test
    result_headers = remove_entity_headers(headers)

    # Verify: Check that the correct headers are removed and allowed ones are kept
    assert 'Content-Type' in result_headers
    assert 'Content-Length' not in result_headers
    assert 'Content-Location' in result_headers
    assert 'Expires' in result_headers
    assert 'Last-Modified' not in result_headers

    # Cleanup: No cleanup required as the mock is scoped to the test function
