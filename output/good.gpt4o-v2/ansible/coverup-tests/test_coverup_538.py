# file: lib/ansible/plugins/callback/junit.py:340-350
# asked: {"lines": [340, 341, 345, 346, 347, 348, 349, 350], "branches": []}
# gained: {"lines": [340, 341, 345, 346, 347, 348, 349, 350], "branches": []}

import pytest
import time
from unittest import mock

def test_host_data_initialization():
    import ansible.plugins.callback.junit as junit

    uuid = "1234"
    name = "test_host"
    status = "SUCCESS"
    result = {"key": "value"}

    with mock.patch('time.time', return_value=1234567890):
        host_data = junit.HostData(uuid, name, status, result)

    assert host_data.uuid == uuid
    assert host_data.name == name
    assert host_data.status == status
    assert host_data.result == result
    assert host_data.finish == 1234567890
