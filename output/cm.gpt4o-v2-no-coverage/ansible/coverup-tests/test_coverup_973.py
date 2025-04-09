# file: lib/ansible/modules/systemd.py:291-292
# asked: {"lines": [291, 292], "branches": []}
# gained: {"lines": [291, 292], "branches": []}

import pytest

from ansible.modules.systemd import is_deactivating_service

def test_is_deactivating_service():
    # Test when service is deactivating
    service_status = {'ActiveState': 'deactivating'}
    assert is_deactivating_service(service_status) == True

    # Test when service is not deactivating
    service_status = {'ActiveState': 'active'}
    assert is_deactivating_service(service_status) == False

    # Test when service status does not contain 'ActiveState'
    service_status = {}
    with pytest.raises(KeyError):
        is_deactivating_service(service_status)
