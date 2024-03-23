# file lib/ansible/modules/systemd.py:287-288
# lines [287, 288]
# branches []

import pytest
from ansible.modules.systemd import is_running_service

@pytest.fixture
def mock_service_status(mocker):
    # Mock the service_status dictionary
    return mocker.MagicMock()

def test_is_running_service_active(mock_service_status):
    # Set the mock to return 'active' for 'ActiveState'
    mock_service_status.__getitem__.return_value = 'active'
    assert is_running_service(mock_service_status) == True

def test_is_running_service_activating(mock_service_status):
    # Set the mock to return 'activating' for 'ActiveState'
    mock_service_status.__getitem__.return_value = 'activating'
    assert is_running_service(mock_service_status) == True

def test_is_running_service_inactive(mock_service_status):
    # Set the mock to return 'inactive' for 'ActiveState'
    mock_service_status.__getitem__.return_value = 'inactive'
    assert is_running_service(mock_service_status) == False

def test_is_running_service_failed(mock_service_status):
    # Set the mock to return 'failed' for 'ActiveState'
    mock_service_status.__getitem__.return_value = 'failed'
    assert is_running_service(mock_service_status) == False

# Ensure that the mock_service_status fixture is used for all tests
pytest.mark.usefixtures("mock_service_status")
