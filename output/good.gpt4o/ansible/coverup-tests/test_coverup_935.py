# file lib/ansible/module_utils/urls.py:1511-1519
# lines [1511, 1519]
# branches []

import pytest
from unittest.mock import patch, MagicMock

# Assuming the Request class is imported from ansible.module_utils.urls
from ansible.module_utils.urls import Request

@pytest.fixture
def mock_open(mocker):
    return mocker.patch('ansible.module_utils.urls.Request.open', return_value='HTTPResponse')

def test_delete_request(mock_open):
    request = Request()
    url = 'http://example.com'
    response = request.delete(url, param1='value1', param2='value2')
    
    # Verify that the open method was called with the correct parameters
    mock_open.assert_called_once_with('DELETE', url, param1='value1', param2='value2')
    
    # Verify the response
    assert response == 'HTTPResponse'
