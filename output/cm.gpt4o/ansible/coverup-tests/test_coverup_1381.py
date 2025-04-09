# file lib/ansible/inventory/manager.py:617-644
# lines [624, 625, 627, 628, 630, 631, 632, 634, 635, 636, 637, 638, 639, 640, 641, 643, 644]
# branches ['624->625', '624->627', '630->631', '630->644', '631->632', '631->634', '634->635', '634->643', '636->637', '636->638', '638->639', '638->640']

import os
import pytest
from unittest import mock
from ansible.inventory.manager import InventoryManager
from ansible.errors import AnsibleError
from ansible.module_utils._text import to_bytes, to_text

def split_host_pattern(pattern):
    return pattern.split(',')

class MockLoader:
    pass

@pytest.fixture
def inventory_manager():
    return InventoryManager(loader=MockLoader())

def test_subset_with_none_pattern(inventory_manager):
    inventory_manager.subset(None)
    assert inventory_manager._subset is None

def test_subset_with_empty_pattern(inventory_manager):
    inventory_manager.subset('')
    assert inventory_manager._subset == []

def test_subset_with_valid_pattern(inventory_manager):
    inventory_manager.subset('host1,host2')
    assert inventory_manager._subset == ['host1', 'host2']

def test_subset_with_at_file_pattern(inventory_manager, tmpdir):
    limit_file = tmpdir.join("limit_file.txt")
    limit_file.write("host1\nhost2")
    inventory_manager.subset(f'@{limit_file}')
    assert inventory_manager._subset == ['host1', 'host2']

def test_subset_with_nonexistent_file(inventory_manager):
    with pytest.raises(AnsibleError, match=r'Unable to find limit file'):
        inventory_manager.subset('@nonexistent_file.txt')

def test_subset_with_directory(inventory_manager, tmpdir):
    limit_dir = tmpdir.mkdir("limit_dir")
    with pytest.raises(AnsibleError, match=r'Limit starting with "@" must be a file, not a directory'):
        inventory_manager.subset(f'@{limit_dir}')

def test_subset_with_mixed_patterns(inventory_manager, tmpdir):
    limit_file = tmpdir.join("limit_file.txt")
    limit_file.write("host1\nhost2")
    inventory_manager.subset(f'host3,@{limit_file},host4')
    assert inventory_manager._subset == ['host3', 'host1', 'host2', 'host4']
