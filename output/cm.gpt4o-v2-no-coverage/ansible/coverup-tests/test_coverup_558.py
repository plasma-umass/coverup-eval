# file: lib/ansible/plugins/callback/junit.py:340-350
# asked: {"lines": [340, 341, 345, 346, 347, 348, 349, 350], "branches": []}
# gained: {"lines": [340, 341, 345, 346, 347, 348, 349, 350], "branches": []}

import pytest
import time
from ansible.plugins.callback.junit import HostData

def test_host_data_initialization(monkeypatch):
    # Mock time.time to return a fixed value
    fixed_time = 1609459200.0  # This is 2021-01-01 00:00:00 UTC
    monkeypatch.setattr(time, 'time', lambda: fixed_time)
    
    # Create an instance of HostData
    uuid = "1234"
    name = "test_host"
    status = "SUCCESS"
    result = {"key": "value"}
    
    host_data = HostData(uuid, name, status, result)
    
    # Assertions to verify the initialization
    assert host_data.uuid == uuid
    assert host_data.name == name
    assert host_data.status == status
    assert host_data.result == result
    assert host_data.finish == fixed_time
