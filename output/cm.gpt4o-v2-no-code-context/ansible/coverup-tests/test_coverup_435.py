# file: lib/ansible/plugins/callback/junit.py:340-350
# asked: {"lines": [340, 341, 345, 346, 347, 348, 349, 350], "branches": []}
# gained: {"lines": [340, 341, 345, 346, 347, 348, 349, 350], "branches": []}

import pytest
import time
from ansible.plugins.callback.junit import HostData

@pytest.fixture
def mock_time(monkeypatch):
    mock_time = 1234567890.0
    monkeypatch.setattr(time, 'time', lambda: mock_time)
    return mock_time

def test_host_data_initialization(mock_time):
    uuid = "1234"
    name = "test_host"
    status = "ok"
    result = "success"

    host_data = HostData(uuid, name, status, result)

    assert host_data.uuid == uuid
    assert host_data.name == name
    assert host_data.status == status
    assert host_data.result == result
    assert host_data.finish == mock_time
