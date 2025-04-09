# file mimesis/providers/internet.py:69-77
# lines [77]
# branches []

import pytest
from mimesis.providers.internet import Internet

# Mock the HTTP_STATUS_CODES to contain a controlled set of status codes
@pytest.fixture
def mock_http_status_codes(mocker):
    mock_status_codes = [200, 404, 500]
    mocker.patch('mimesis.providers.internet.HTTP_STATUS_CODES', new=mock_status_codes)
    return mock_status_codes

# Test function to cover line 77
def test_http_status_code(mock_http_status_codes):
    internet_provider = Internet()
    status_code = internet_provider.http_status_code()
    
    # Assert that the returned status code is one of the mocked status codes
    assert status_code in mock_http_status_codes
