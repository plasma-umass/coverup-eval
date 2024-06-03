# file lib/ansible/module_utils/facts/system/ssh_pub_keys.py:24-54
# lines [54]
# branches ['40->54']

import pytest
from unittest.mock import patch, mock_open

# Assuming the SshPubKeyFactCollector and get_file_content are imported from the module
from ansible.module_utils.facts.system.ssh_pub_keys import SshPubKeyFactCollector, get_file_content

@pytest.fixture
def mock_get_file_content():
    with patch('ansible.module_utils.facts.system.ssh_pub_keys.get_file_content') as mock:
        yield mock

def test_collect_no_keys_found(mock_get_file_content):
    # Mock get_file_content to return None for all key files
    mock_get_file_content.return_value = None

    collector = SshPubKeyFactCollector()
    result = collector.collect()

    # Assert that the result is an empty dictionary since no keys were found
    assert result == {}

def test_collect_keys_found(mock_get_file_content):
    # Mock get_file_content to return valid key data for one of the key files
    mock_get_file_content.side_effect = lambda filename: "ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEAr" if 'rsa' in filename else None

    collector = SshPubKeyFactCollector()
    result = collector.collect()

    # Assert that the result contains the expected key data
    assert 'ssh_host_key_rsa_public' in result
    assert result['ssh_host_key_rsa_public'] == 'AAAAB3NzaC1yc2EAAAABIwAAAQEAr'
    assert result['ssh_host_key_rsa_public_keytype'] == 'ssh-rsa'

def test_collect_partial_keys_found(mock_get_file_content):
    # Mock get_file_content to return valid key data for some of the key files
    def mock_get_file_content_side_effect(filename):
        if 'rsa' in filename:
            return "ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEAr"
        elif 'ecdsa' in filename:
            return "ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBB"
        return None

    mock_get_file_content.side_effect = mock_get_file_content_side_effect

    collector = SshPubKeyFactCollector()
    result = collector.collect()

    # Assert that the result contains the expected key data
    assert 'ssh_host_key_rsa_public' in result
    assert result['ssh_host_key_rsa_public'] == 'AAAAB3NzaC1yc2EAAAABIwAAAQEAr'
    assert result['ssh_host_key_rsa_public_keytype'] == 'ssh-rsa'
    assert 'ssh_host_key_ecdsa_public' in result
    assert result['ssh_host_key_ecdsa_public'] == 'AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBB'
    assert result['ssh_host_key_ecdsa_public_keytype'] == 'ecdsa-sha2-nistp256'
    assert 'ssh_host_key_dsa_public' not in result
    assert 'ssh_host_key_ed25519_public' not in result
