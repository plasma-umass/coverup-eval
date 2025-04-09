# file lib/ansible/inventory/host.py:102-103
# lines [103]
# branches []

import pytest
from unittest.mock import patch

# Assuming the Host class is imported from ansible.inventory.host
from ansible.inventory.host import Host

def test_get_name():
    host = Host()
    with patch.object(host, 'name', 'test_host'):
        assert host.get_name() == 'test_host'
