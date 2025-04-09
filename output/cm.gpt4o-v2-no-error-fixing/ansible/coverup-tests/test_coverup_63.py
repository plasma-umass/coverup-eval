# file: lib/ansible/module_utils/facts/system/ssh_pub_keys.py:24-54
# asked: {"lines": [24, 25, 26, 32, 33, 34, 38, 40, 41, 42, 43, 46, 47, 48, 49, 50, 51, 52, 54], "branches": [[40, 41], [40, 54], [41, 40], [41, 42], [43, 46], [43, 47], [49, 41], [49, 50]]}
# gained: {"lines": [24, 25, 26, 32, 33, 34, 38, 40, 41, 42, 43, 46, 47, 48, 49, 50, 51, 52, 54], "branches": [[40, 41], [40, 54], [41, 40], [41, 42], [43, 46], [43, 47], [49, 41], [49, 50]]}

import pytest
from unittest.mock import patch, mock_open
from ansible.module_utils.facts.system.ssh_pub_keys import SshPubKeyFactCollector

@pytest.fixture
def mock_get_file_content():
    with patch('ansible.module_utils.facts.system.ssh_pub_keys.get_file_content') as mock:
        yield mock

def test_collect_all_keys_found(mock_get_file_content):
    mock_get_file_content.side_effect = [
        "ssh-dss AAAAB3NzaC1kc3MAAACB...",
        "ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQE...",
        "ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBB...",
        "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAI..."
    ]
    
    collector = SshPubKeyFactCollector()
    facts = collector.collect()
    
    assert facts['ssh_host_key_dsa_public'] == "AAAAB3NzaC1kc3MAAACB..."
    assert facts['ssh_host_key_dsa_public_keytype'] == "ssh-dss"
    assert facts['ssh_host_key_rsa_public'] == "AAAAB3NzaC1yc2EAAAABIwAAAQE..."
    assert facts['ssh_host_key_rsa_public_keytype'] == "ssh-rsa"
    assert facts['ssh_host_key_ecdsa_public'] == "AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBB..."
    assert facts['ssh_host_key_ecdsa_public_keytype'] == "ecdsa-sha2-nistp256"
    assert facts['ssh_host_key_ed25519_public'] == "AAAAC3NzaC1lZDI1NTE5AAAAI..."
    assert facts['ssh_host_key_ed25519_public_keytype'] == "ssh-ed25519"

def test_collect_no_keys_found(mock_get_file_content):
    mock_get_file_content.return_value = None
    
    collector = SshPubKeyFactCollector()
    facts = collector.collect()
    
    assert facts == {}

def test_collect_partial_keys_found(mock_get_file_content):
    mock_get_file_content.side_effect = [
        "ssh-dss AAAAB3NzaC1kc3MAAACB...",
        None,
        "ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBB...",
        None
    ]
    
    collector = SshPubKeyFactCollector()
    facts = collector.collect()
    
    assert facts['ssh_host_key_dsa_public'] == "AAAAB3NzaC1kc3MAAACB..."
    assert facts['ssh_host_key_dsa_public_keytype'] == "ssh-dss"
    assert 'ssh_host_key_rsa_public' not in facts
    assert facts['ssh_host_key_ecdsa_public'] == "AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBB..."
    assert facts['ssh_host_key_ecdsa_public_keytype'] == "ecdsa-sha2-nistp256"
    assert 'ssh_host_key_ed25519_public' not in facts
