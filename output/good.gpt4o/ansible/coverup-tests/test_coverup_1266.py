# file lib/ansible/plugins/inventory/auto.py:30-62
# lines [44, 45]
# branches []

import pytest
from unittest.mock import Mock, patch
from ansible.plugins.inventory.auto import InventoryModule
from ansible.errors import AnsibleParserError

@pytest.fixture
def mock_loader():
    return Mock()

@pytest.fixture
def mock_inventory():
    return Mock()

def test_parse_attribute_error(mock_loader, mock_inventory):
    inventory_module = InventoryModule()
    path = 'test_inventory.yml'

    # Mock the loader to return an object that raises AttributeError on get
    mock_loader.load_from_file.return_value = Mock(get=Mock(side_effect=AttributeError))

    with pytest.raises(AnsibleParserError, match="no root 'plugin' key found"):
        inventory_module.parse(mock_inventory, mock_loader, path)

    mock_loader.load_from_file.assert_called_once_with(path, cache=False)

# Clean up after the test
@pytest.fixture(autouse=True)
def cleanup():
    yield
    # Add any necessary cleanup code here
