# file lib/ansible/module_utils/facts/hardware/netbsd.py:114-135
# lines [122]
# branches ['121->122']

import pytest
from ansible.module_utils.facts.hardware.netbsd import NetBSDHardware
from unittest.mock import MagicMock

# Mock the get_file_content function to return None
def mock_get_file_content_none(file_path):
    return None

# Test function to cover line 122
def test_get_mount_facts_with_no_fstab(mocker):
    mocker.patch('ansible.module_utils.facts.hardware.netbsd.get_file_content', side_effect=mock_get_file_content_none)
    mocker.patch('ansible.module_utils.facts.hardware.netbsd.get_mount_size', return_value={})

    module_mock = MagicMock()
    netbsd_hardware = NetBSDHardware(module=module_mock)
    mount_facts = netbsd_hardware.get_mount_facts()

    assert 'mounts' in mount_facts
    assert mount_facts['mounts'] == []
