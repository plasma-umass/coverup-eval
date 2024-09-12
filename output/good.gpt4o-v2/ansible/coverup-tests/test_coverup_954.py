# file: lib/ansible/modules/systemd.py:287-288
# asked: {"lines": [287, 288], "branches": []}
# gained: {"lines": [287, 288], "branches": []}

import pytest
from ansible.modules.systemd import is_running_service

def test_is_running_service_active():
    service_status = {'ActiveState': 'active'}
    assert is_running_service(service_status) == True

def test_is_running_service_activating():
    service_status = {'ActiveState': 'activating'}
    assert is_running_service(service_status) == True

def test_is_running_service_inactive():
    service_status = {'ActiveState': 'inactive'}
    assert is_running_service(service_status) == False

def test_is_running_service_failed():
    service_status = {'ActiveState': 'failed'}
    assert is_running_service(service_status) == False
