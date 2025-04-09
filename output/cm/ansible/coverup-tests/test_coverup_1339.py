# file lib/ansible/plugins/callback/junit.py:340-350
# lines [346, 347, 348, 349, 350]
# branches []

import time
from unittest.mock import patch
import pytest

# Assuming the HostData class is in a module named junit
from ansible.plugins.callback.junit import HostData

@pytest.fixture
def mock_time(mocker):
    mock = mocker.patch('ansible.plugins.callback.junit.time.time', return_value=1234567890.0)
    return mock

def test_host_data_initialization(mock_time):
    uuid = "test-uuid"
    name = "test-name"
    status = "test-status"
    result = "test-result"
    
    host_data = HostData(uuid, name, status, result)
    
    assert host_data.uuid == uuid
    assert host_data.name == name
    assert host_data.status == status
    assert host_data.result == result
    assert host_data.finish == 1234567890.0
    mock_time.assert_called_once()
