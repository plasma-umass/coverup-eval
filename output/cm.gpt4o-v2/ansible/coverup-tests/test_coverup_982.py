# file: lib/ansible/module_utils/urls.py:1511-1519
# asked: {"lines": [1511, 1519], "branches": []}
# gained: {"lines": [1511, 1519], "branches": []}

import pytest
from ansible.module_utils.urls import Request

@pytest.fixture
def request_instance():
    return Request()

def test_delete_method(request_instance, mocker):
    mock_open = mocker.patch.object(request_instance, 'open', return_value='mocked_response')
    url = 'http://example.com'
    response = request_instance.delete(url)
    
    mock_open.assert_called_once_with('DELETE', url)
    assert response == 'mocked_response'
