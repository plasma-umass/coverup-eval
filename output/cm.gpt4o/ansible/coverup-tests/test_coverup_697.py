# file lib/ansible/plugins/inventory/yaml.py:171-177
# lines [171, 175, 177]
# branches []

import pytest
from ansible.plugins.inventory.yaml import InventoryModule
from unittest.mock import patch

@pytest.fixture
def inventory_module():
    return InventoryModule()

def test_parse_host(inventory_module, mocker):
    host_pattern = 'localhost:22'
    expected_hostnames = ['localhost']
    expected_port = 22

    mock_expand_hostpattern = mocker.patch.object(inventory_module, '_expand_hostpattern', return_value=(expected_hostnames, expected_port))

    hostnames, port = inventory_module._parse_host(host_pattern)

    mock_expand_hostpattern.assert_called_once_with(host_pattern)
    assert hostnames == expected_hostnames
    assert port == expected_port
