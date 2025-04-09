# file lib/ansible/inventory/manager.py:617-644
# lines [624, 625, 627, 628, 630, 631, 632, 634, 635, 636, 637, 638, 639, 640, 641, 643, 644]
# branches ['624->625', '624->627', '630->631', '630->644', '631->632', '631->634', '634->635', '634->643', '636->637', '636->638', '638->639', '638->640']

import os
import pytest
from ansible.errors import AnsibleError
from ansible.inventory.manager import InventoryManager
from ansible.module_utils._text import to_bytes, to_text

def test_inventory_manager_subset_with_limit_file(mocker, tmp_path):
    # Setup
    inventory_manager = InventoryManager(loader=None, sources=None)
    subset_file = tmp_path / "subset.txt"
    subset_file.write_text(u"host1\nhost2\n")

    # Mock the os.path.exists and os.path.isfile to return True
    mocker.patch('os.path.exists', return_value=True)
    mocker.patch('os.path.isfile', return_value=True)

    # Test
    inventory_manager.subset('@' + str(subset_file))

    # Assert
    # The file read adds an empty string at the end due to the trailing newline
    assert inventory_manager._subset == ['host1', 'host2', '']

def test_inventory_manager_subset_with_nonexistent_limit_file(mocker):
    # Setup
    inventory_manager = InventoryManager(loader=None, sources=None)
    non_existent_file = "/nonexistent/limit_file"

    # Mock the os.path.exists to return False
    mocker.patch('os.path.exists', return_value=False)

    # Test and Assert
    with pytest.raises(AnsibleError) as excinfo:
        inventory_manager.subset('@' + non_existent_file)
    assert 'Unable to find limit file' in str(excinfo.value)

def test_inventory_manager_subset_with_directory_limit(mocker, tmp_path):
    # Setup
    inventory_manager = InventoryManager(loader=None, sources=None)
    subset_dir = tmp_path / "subset_dir"
    subset_dir.mkdir()

    # Mock the os.path.exists and os.path.isfile
    mocker.patch('os.path.exists', return_value=True)
    mocker.patch('os.path.isfile', return_value=False)

    # Test and Assert
    with pytest.raises(AnsibleError) as excinfo:
        inventory_manager.subset('@' + str(subset_dir))
    assert 'must be a file, not a directory' in str(excinfo.value)

def test_inventory_manager_subset_with_empty_pattern(mocker):
    # Setup
    inventory_manager = InventoryManager(loader=None, sources=None)

    # Test
    inventory_manager.subset('')

    # Assert
    assert inventory_manager._subset == []

def test_inventory_manager_subset_with_none_pattern():
    # Setup
    inventory_manager = InventoryManager(loader=None, sources=None)

    # Test
    inventory_manager.subset(None)

    # Assert
    assert inventory_manager._subset is None
