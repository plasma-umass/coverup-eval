# file mimesis/providers/internet.py:59-67
# lines [67]
# branches []

import pytest
from mimesis.providers.internet import Internet

# Mock the HTTP_STATUS_MSGS to ensure the test is deterministic
@pytest.fixture
def mock_http_status_msgs(mocker):
    mock_msgs = ["200 OK", "404 Not Found", "500 Internal Server Error"]
    mocker.patch('mimesis.providers.internet.HTTP_STATUS_MSGS', new=mock_msgs)
    return mock_msgs

def test_http_status_message(mock_http_status_msgs):
    internet = Internet()
    message = internet.http_status_message()
    assert message in mock_http_status_msgs
