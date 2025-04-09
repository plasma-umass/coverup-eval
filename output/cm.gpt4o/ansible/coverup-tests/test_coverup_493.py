# file lib/ansible/plugins/callback/junit.py:340-350
# lines [340, 341, 345, 346, 347, 348, 349, 350]
# branches []

import pytest
import time
from unittest.mock import patch

# Assuming the HostData class is imported from ansible.plugins.callback.junit
from ansible.plugins.callback.junit import HostData

@pytest.fixture
def mock_time():
    with patch('time.time', return_value=1234567890.0):
        yield

def test_host_data_initialization(mock_time):
    uuid = "1234-5678-9012"
    name = "test_host"
    status = "SUCCESS"
    result = {"changed": True}

    host_data = HostData(uuid, name, status, result)

    assert host_data.uuid == uuid
    assert host_data.name == name
    assert host_data.status == status
    assert host_data.result == result
    assert host_data.finish == 1234567890.0
