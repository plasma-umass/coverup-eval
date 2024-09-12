# file: lib/ansible/modules/systemd.py:287-288
# asked: {"lines": [287, 288], "branches": []}
# gained: {"lines": [287, 288], "branches": []}

import pytest

def test_is_running_service_active():
    from ansible.modules.systemd import is_running_service
    service_status = {'ActiveState': 'active'}
    assert is_running_service(service_status) == True

def test_is_running_service_activating():
    from ansible.modules.systemd import is_running_service
    service_status = {'ActiveState': 'activating'}
    assert is_running_service(service_status) == True

def test_is_running_service_inactive():
    from ansible.modules.systemd import is_running_service
    service_status = {'ActiveState': 'inactive'}
    assert is_running_service(service_status) == False

def test_is_running_service_failed():
    from ansible.modules.systemd import is_running_service
    service_status = {'ActiveState': 'failed'}
    assert is_running_service(service_status) == False

def test_is_running_service_unknown_state():
    from ansible.modules.systemd import is_running_service
    service_status = {'ActiveState': 'unknown'}
    assert is_running_service(service_status) == False
