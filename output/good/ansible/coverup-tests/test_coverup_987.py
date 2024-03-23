# file lib/ansible/modules/systemd.py:291-292
# lines [291, 292]
# branches []

import pytest
from ansible.modules.systemd import is_deactivating_service

@pytest.fixture
def mock_service_status(mocker):
    return mocker.MagicMock()

def test_is_deactivating_service_true(mock_service_status):
    mock_service_status.return_value = {'ActiveState': 'deactivating'}
    assert is_deactivating_service(mock_service_status.return_value) is True

def test_is_deactivating_service_false(mock_service_status):
    mock_service_status.return_value = {'ActiveState': 'active'}
    assert is_deactivating_service(mock_service_status.return_value) is False
