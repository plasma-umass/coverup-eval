# file lib/ansible/module_utils/urls.py:1478-1487
# lines [1478, 1487]
# branches []

import pytest
from unittest.mock import patch, MagicMock

# Assuming the Request class is imported from ansible.module_utils.urls
from ansible.module_utils.urls import Request

@pytest.fixture
def mock_http_response():
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.read.return_value = b'{"success": true}'
    return mock_response

def test_request_post(mocker, mock_http_response):
    mock_open = mocker.patch('ansible.module_utils.urls.Request.open', return_value=mock_http_response)
    
    request = Request()
    url = 'http://example.com/api'
    data = b'{"key": "value"}'
    
    response = request.post(url, data=data)
    
    mock_open.assert_called_once_with('POST', url, data=data)
    assert response.status_code == 200
    assert response.read() == b'{"success": true}'
