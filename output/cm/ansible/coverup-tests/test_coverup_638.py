# file lib/ansible/parsing/yaml/objects.py:185-188
# lines [185, 186, 187, 188]
# branches ['186->187', '186->188']

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

@pytest.fixture
def vault_encrypted_unicode():
    # Setup
    vault_str = AnsibleVaultEncryptedUnicode('encrypted_data')
    yield vault_str
    # Teardown (nothing to do here since we're not creating any persistent state)

def test_ansible_vault_encrypted_unicode_contains(vault_encrypted_unicode):
    # Test with a character that is in the data
    assert 'e' in vault_encrypted_unicode

    # Test with a character that is not in the data
    assert 'z' not in vault_encrypted_unicode

    # Test with an instance of AnsibleVaultEncryptedUnicode that has matching data
    another_vault_str = AnsibleVaultEncryptedUnicode('encrypted_data')
    assert another_vault_str in vault_encrypted_unicode

    # Test with an instance of AnsibleVaultEncryptedUnicode that has non-matching data
    different_vault_str = AnsibleVaultEncryptedUnicode('different_data')
    assert different_vault_str not in vault_encrypted_unicode
