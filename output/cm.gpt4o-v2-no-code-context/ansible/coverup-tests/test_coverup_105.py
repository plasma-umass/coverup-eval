# file: lib/ansible/module_utils/facts/hardware/netbsd.py:114-135
# asked: {"lines": [114, 115, 116, 118, 119, 121, 122, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135], "branches": [[121, 122], [121, 124], [124, 125], [124, 135], [125, 126], [125, 127]]}
# gained: {"lines": [114, 115, 116, 118, 119, 121, 122, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135], "branches": [[121, 122], [121, 124], [124, 125], [124, 135], [125, 126], [125, 127]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.module_utils.facts.hardware.netbsd import NetBSDHardware

@pytest.fixture
def netbsd_hardware():
    # Mock the module argument required by the Hardware base class
    module_mock = MagicMock()
    return NetBSDHardware(module=module_mock)

def test_get_mount_facts_empty_fstab(netbsd_hardware, monkeypatch):
    # Mock get_file_content to return an empty string
    monkeypatch.setattr('ansible.module_utils.facts.hardware.netbsd.get_file_content', lambda x: '')
    
    result = netbsd_hardware.get_mount_facts()
    
    assert result == {'mounts': []}

def test_get_mount_facts_with_comments_and_empty_lines(netbsd_hardware, monkeypatch):
    fstab_content = """
# This is a comment
/dev/sd0a / ffs rw 1 1

# Another comment
/dev/sd0b /home ffs rw 1 2
"""
    # Mock get_file_content to return the fstab_content
    monkeypatch.setattr('ansible.module_utils.facts.hardware.netbsd.get_file_content', lambda x: fstab_content)
    # Mock get_mount_size to return a dummy dictionary
    monkeypatch.setattr('ansible.module_utils.facts.hardware.netbsd.get_mount_size', lambda x: {'size': '100G', 'used': '50G', 'available': '50G'})
    
    result = netbsd_hardware.get_mount_facts()
    
    expected_mounts = [
        {
            'mount': '/',
            'device': '/dev/sd0a',
            'fstype': 'ffs',
            'options': 'rw',
            'size': '100G',
            'used': '50G',
            'available': '50G'
        },
        {
            'mount': '/home',
            'device': '/dev/sd0b',
            'fstype': 'ffs',
            'options': 'rw',
            'size': '100G',
            'used': '50G',
            'available': '50G'
        }
    ]
    
    assert result == {'mounts': expected_mounts}

def test_get_mount_facts_with_valid_entries(netbsd_hardware, monkeypatch):
    fstab_content = """
/dev/sd0a / ffs rw 1 1
/dev/sd0b /home ffs rw 1 2
"""
    # Mock get_file_content to return the fstab_content
    monkeypatch.setattr('ansible.module_utils.facts.hardware.netbsd.get_file_content', lambda x: fstab_content)
    # Mock get_mount_size to return a dummy dictionary
    monkeypatch.setattr('ansible.module_utils.facts.hardware.netbsd.get_mount_size', lambda x: {'size': '100G', 'used': '50G', 'available': '50G'})
    
    result = netbsd_hardware.get_mount_facts()
    
    expected_mounts = [
        {
            'mount': '/',
            'device': '/dev/sd0a',
            'fstype': 'ffs',
            'options': 'rw',
            'size': '100G',
            'used': '50G',
            'available': '50G'
        },
        {
            'mount': '/home',
            'device': '/dev/sd0b',
            'fstype': 'ffs',
            'options': 'rw',
            'size': '100G',
            'used': '50G',
            'available': '50G'
        }
    ]
    
    assert result == {'mounts': expected_mounts}
