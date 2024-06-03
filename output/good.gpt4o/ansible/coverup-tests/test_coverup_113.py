# file lib/ansible/module_utils/facts/system/ssh_pub_keys.py:24-54
# lines [24, 25, 26, 32, 33, 34, 38, 40, 41, 42, 43, 46, 47, 48, 49, 50, 51, 52, 54]
# branches ['40->41', '40->54', '41->40', '41->42', '43->46', '43->47', '49->41', '49->50']

import pytest
from unittest.mock import patch, mock_open

# Assuming the SshPubKeyFactCollector and get_file_content are imported from the module
from ansible.module_utils.facts.system.ssh_pub_keys import SshPubKeyFactCollector

@pytest.fixture
def mock_get_file_content():
    with patch('ansible.module_utils.facts.system.ssh_pub_keys.get_file_content') as mock:
        yield mock

def test_collect_ssh_pub_keys(mock_get_file_content):
    # Mock the return values for get_file_content
    mock_get_file_content.side_effect = [
        "ssh-dss AAAAB3NzaC1kc3MAAACBAP1...",  # dsa key
        None,  # rsa key not found
        None,  # ecdsa key not found
        None,  # ed25519 key not found
    ]

    collector = SshPubKeyFactCollector()
    facts = collector.collect()

    assert 'ssh_host_key_dsa_public' in facts
    assert facts['ssh_host_key_dsa_public'] == 'AAAAB3NzaC1kc3MAAACBAP1...'
    assert 'ssh_host_key_dsa_public_keytype' in facts
    assert facts['ssh_host_key_dsa_public_keytype'] == 'ssh-dss'

    assert 'ssh_host_key_rsa_public' not in facts
    assert 'ssh_host_key_ecdsa_public' not in facts
    assert 'ssh_host_key_ed25519_public' not in facts

    # Ensure the mock was called with the expected filenames
    mock_get_file_content.assert_any_call('/etc/ssh/ssh_host_dsa_key.pub')
    mock_get_file_content.assert_any_call('/etc/ssh/ssh_host_rsa_key.pub')
    mock_get_file_content.assert_any_call('/etc/ssh/ssh_host_ecdsa_key.pub')
    mock_get_file_content.assert_any_call('/etc/ssh/ssh_host_ed25519_key.pub')
