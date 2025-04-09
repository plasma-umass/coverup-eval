# file: lib/ansible/modules/systemd.py:291-292
# asked: {"lines": [291, 292], "branches": []}
# gained: {"lines": [291, 292], "branches": []}

import pytest

from ansible.modules.systemd import is_deactivating_service

def test_is_deactivating_service_true():
    service_status = {'ActiveState': 'deactivating'}
    assert is_deactivating_service(service_status) == True

def test_is_deactivating_service_false():
    service_status = {'ActiveState': 'active'}
    assert is_deactivating_service(service_status) == False

def test_is_deactivating_service_empty():
    service_status = {'ActiveState': ''}
    assert is_deactivating_service(service_status) == False

def test_is_deactivating_service_missing_key():
    service_status = {}
    with pytest.raises(KeyError):
        is_deactivating_service(service_status)
