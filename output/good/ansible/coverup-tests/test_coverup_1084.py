# file lib/ansible/parsing/yaml/objects.py:259-260
# lines [259, 260]
# branches []

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

@pytest.fixture
def vault_encrypted_unicode():
    # Setup
    vault_str = AnsibleVaultEncryptedUnicode('!vault |')
    vault_str._ciphertext = "EncryptedData123"
    yield vault_str
    # Teardown
    vault_str._ciphertext = None

def test_ansible_vault_encrypted_unicode_isalpha(vault_encrypted_unicode):
    # Test with non-alpha characters
    vault_encrypted_unicode._ciphertext = "EncryptedData123"
    assert not vault_encrypted_unicode.isalpha()

    # Test with alpha characters only
    vault_encrypted_unicode._ciphertext = "EncryptedData"
    assert vault_encrypted_unicode.isalpha()
