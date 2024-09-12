# file: lib/ansible/plugins/callback/junit.py:340-350
# asked: {"lines": [340, 341, 345, 346, 347, 348, 349, 350], "branches": []}
# gained: {"lines": [340, 341, 345, 346, 347, 348, 349, 350], "branches": []}

import pytest
import time
from ansible.plugins.callback.junit import HostData

@pytest.fixture
def mock_time(monkeypatch):
    class MockTime:
        def __init__(self):
            self.current_time = 1234567890.0

        def time(self):
            return self.current_time

    mock_time = MockTime()
    monkeypatch.setattr(time, 'time', mock_time.time)
    return mock_time

def test_host_data_initialization(mock_time):
    uuid = "1234"
    name = "test_host"
    status = "SUCCESS"
    result = {"key": "value"}

    host_data = HostData(uuid, name, status, result)

    assert host_data.uuid == uuid
    assert host_data.name == name
    assert host_data.status == status
    assert host_data.result == result
    assert host_data.finish == mock_time.current_time
