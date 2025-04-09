# file: lib/ansible/module_utils/facts/system/ssh_pub_keys.py:24-54
# asked: {"lines": [24, 25, 26, 32, 33, 34, 38, 40, 41, 42, 43, 46, 47, 48, 49, 50, 51, 52, 54], "branches": [[40, 41], [40, 54], [41, 40], [41, 42], [43, 46], [43, 47], [49, 41], [49, 50]]}
# gained: {"lines": [24, 25, 26, 32, 33, 34, 38, 40, 41, 42, 43, 46, 47, 48, 49, 50, 51, 52, 54], "branches": [[40, 41], [40, 54], [41, 40], [41, 42], [43, 46], [43, 47], [49, 41], [49, 50]]}

import pytest
from unittest.mock import patch, mock_open

# Assuming the SshPubKeyFactCollector and get_file_content are imported from the module
from ansible.module_utils.facts.system.ssh_pub_keys import SshPubKeyFactCollector, get_file_content

@pytest.fixture
def mock_get_file_content():
    with patch('ansible.module_utils.facts.system.ssh_pub_keys.get_file_content') as mock:
        yield mock

def test_collect_no_keys_found(mock_get_file_content):
    mock_get_file_content.return_value = None
    collector = SshPubKeyFactCollector()
    result = collector.collect()
    assert result == {}

def test_collect_keys_found(mock_get_file_content):
    key_data = {
        '/etc/ssh/ssh_host_dsa_key.pub': 'ssh-dss AAAAB3NzaC1kc3MAAACB...',
        '/etc/ssh/ssh_host_rsa_key.pub': 'ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQE...',
        '/etc/ssh/ssh_host_ecdsa_key.pub': 'ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBB...',
        '/etc/ssh/ssh_host_ed25519_key.pub': 'ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIB...'
    }

    def side_effect(filename):
        return key_data.get(filename, None)

    mock_get_file_content.side_effect = side_effect

    collector = SshPubKeyFactCollector()
    result = collector.collect()

    expected_result = {
        'ssh_host_key_dsa_public': 'AAAAB3NzaC1kc3MAAACB...',
        'ssh_host_key_dsa_public_keytype': 'ssh-dss',
        'ssh_host_key_rsa_public': 'AAAAB3NzaC1yc2EAAAABIwAAAQE...',
        'ssh_host_key_rsa_public_keytype': 'ssh-rsa',
        'ssh_host_key_ecdsa_public': 'AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBB...',
        'ssh_host_key_ecdsa_public_keytype': 'ecdsa-sha2-nistp256',
        'ssh_host_key_ed25519_public': 'AAAAC3NzaC1lZDI1NTE5AAAAIB...',
        'ssh_host_key_ed25519_public_keytype': 'ssh-ed25519'
    }

    assert result == expected_result

def test_collect_partial_keys_found(mock_get_file_content):
    key_data = {
        '/etc/ssh/ssh_host_dsa_key.pub': 'ssh-dss AAAAB3NzaC1kc3MAAACB...',
        '/etc/ssh/ssh_host_rsa_key.pub': None,
        '/etc/ssh/ssh_host_ecdsa_key.pub': 'ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBB...',
        '/etc/ssh/ssh_host_ed25519_key.pub': None
    }

    def side_effect(filename):
        return key_data.get(filename, None)

    mock_get_file_content.side_effect = side_effect

    collector = SshPubKeyFactCollector()
    result = collector.collect()

    expected_result = {
        'ssh_host_key_dsa_public': 'AAAAB3NzaC1kc3MAAACB...',
        'ssh_host_key_dsa_public_keytype': 'ssh-dss',
        'ssh_host_key_ecdsa_public': 'AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBB...',
        'ssh_host_key_ecdsa_public_keytype': 'ecdsa-sha2-nistp256'
    }

    assert result == expected_result
