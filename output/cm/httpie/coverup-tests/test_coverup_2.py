# file httpie/models.py:5-40
# lines [5, 6, 8, 9, 11, 13, 15, 17, 19, 20, 22, 24, 25, 27, 29, 30, 32, 34, 35, 37, 38, 39, 40]
# branches ['38->39', '38->40']

import pytest
from httpie.models import HTTPMessage
from collections import namedtuple

# Mocking a namedtuple to simulate the original object that HTTPMessage would wrap
MockOriginal = namedtuple('MockOriginal', 'headers')

@pytest.fixture
def mock_http_message(mocker):
    # Mock the original object that HTTPMessage wraps
    mock_orig = MockOriginal(headers={'Content-Type': b'application/json'})
    # Create an instance of the HTTPMessage with the mocked original
    http_message = HTTPMessage(mock_orig)
    return http_message

def test_content_type_with_bytes_header(mock_http_message):
    # Verify that the content_type property decodes bytes to str
    assert mock_http_message.content_type == 'application/json'
