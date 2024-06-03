# file lib/ansible/modules/systemd.py:291-292
# lines [291, 292]
# branches []

import pytest
from unittest.mock import patch

# Assuming the function is_deactivating_service is part of a class or module, 
# we need to import it correctly. For this example, let's assume it's in a module named systemd.

from ansible.modules.systemd import is_deactivating_service

def test_is_deactivating_service():
    # Test case where the service is deactivating
    service_status = {'ActiveState': 'deactivating'}
    assert is_deactivating_service(service_status) == True

    # Test case where the service is not deactivating
    service_status = {'ActiveState': 'active'}
    assert is_deactivating_service(service_status) == False

    # Test case where the service is in an unknown state
    service_status = {'ActiveState': 'unknown'}
    assert is_deactivating_service(service_status) == False
