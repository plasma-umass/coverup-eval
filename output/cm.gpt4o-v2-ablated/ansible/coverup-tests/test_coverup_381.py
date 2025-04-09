# file: lib/ansible/modules/systemd.py:291-292
# asked: {"lines": [291, 292], "branches": []}
# gained: {"lines": [291, 292], "branches": []}

import pytest

from ansible.modules.systemd import is_deactivating_service

def test_is_deactivating_service_active():
    service_status = {'ActiveState': 'deactivating'}
    assert is_deactivating_service(service_status) == True

def test_is_deactivating_service_inactive():
    service_status = {'ActiveState': 'active'}
    assert is_deactivating_service(service_status) == False

def test_is_deactivating_service_other_state():
    service_status = {'ActiveState': 'inactive'}
    assert is_deactivating_service(service_status) == False
