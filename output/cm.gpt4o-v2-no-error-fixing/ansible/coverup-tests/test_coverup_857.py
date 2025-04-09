# file: lib/ansible/module_utils/urls.py:1448-1456
# asked: {"lines": [1456], "branches": []}
# gained: {"lines": [1456], "branches": []}

import pytest
from ansible.module_utils.urls import Request

@pytest.fixture
def request_instance():
    return Request()

def test_get_method_executes_open(request_instance, mocker):
    mock_open = mocker.patch.object(request_instance, 'open', return_value='mocked_response')
    url = 'http://example.com'
    response = request_instance.get(url)
    
    mock_open.assert_called_once_with('GET', url)
    assert response == 'mocked_response'
