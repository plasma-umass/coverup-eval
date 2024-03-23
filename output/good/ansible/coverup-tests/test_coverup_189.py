# file lib/ansible/inventory/manager.py:143-167
# lines [143, 146, 147, 150, 151, 154, 155, 158, 159, 160, 161, 163, 166, 167]
# branches ['158->159', '158->160', '160->161', '160->163', '166->exit', '166->167']

import pytest
from ansible.inventory.manager import InventoryManager
from ansible.parsing.dataloader import DataLoader

@pytest.fixture
def loader():
    return DataLoader()

@pytest.fixture
def inventory_manager(loader):
    return InventoryManager(loader=loader)

def test_inventory_manager_with_none_sources(loader, inventory_manager):
    assert inventory_manager._sources == []

def test_inventory_manager_with_string_sources(loader):
    sources = "localhost,"
    inventory_manager = InventoryManager(loader=loader, sources=sources)
    assert isinstance(inventory_manager._sources, list)
    assert inventory_manager._sources == [sources]

def test_inventory_manager_with_list_sources(loader):
    sources = ["localhost", "example.com"]
    inventory_manager = InventoryManager(loader=loader, sources=sources)
    assert isinstance(inventory_manager._sources, list)
    assert inventory_manager._sources == sources

def test_inventory_manager_parse_sources_called(mocker, loader):
    parse_sources_mock = mocker.patch('ansible.inventory.manager.InventoryManager.parse_sources')
    InventoryManager(loader=loader, sources="localhost,", parse=True)
    parse_sources_mock.assert_called_once_with(cache=True)

def test_inventory_manager_parse_sources_not_called(mocker, loader):
    parse_sources_mock = mocker.patch('ansible.inventory.manager.InventoryManager.parse_sources')
    InventoryManager(loader=loader, sources="localhost,", parse=False)
    parse_sources_mock.assert_not_called()

# Run the tests
def run_tests():
    pytest.main([__file__])

if __name__ == "__main__":
    run_tests()
