# file lib/ansible/parsing/yaml/objects.py:119-122
# lines [119, 120, 121, 122]
# branches ['120->121', '120->122']

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def decrypt(self, ciphertext, obj=None):
        return ciphertext

@pytest.fixture
def vault_encrypted_unicode():
    avu = AnsibleVaultEncryptedUnicode(ciphertext="encrypted data")
    avu.vault = MockVault()
    avu.data = "encrypted data"
    return avu

def test_ansible_vault_encrypted_unicode_eq_with_vault(vault_encrypted_unicode):
    assert vault_encrypted_unicode == "encrypted data"

def test_ansible_vault_encrypted_unicode_eq_without_vault(vault_encrypted_unicode):
    vault_encrypted_unicode.vault = None
    assert not (vault_encrypted_unicode == "encrypted data")
