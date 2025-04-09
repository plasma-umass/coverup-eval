# file lib/ansible/parsing/yaml/objects.py:119-122
# lines [120, 121, 122]
# branches ['120->121', '120->122']

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def __init__(self, data):
        self.data = data

    def decrypt(self, ciphertext, obj=None):
        return self.data

@pytest.fixture
def mock_vault():
    return MockVault(data="decrypted_data")

@pytest.fixture
def ansible_vault_encrypted_unicode(mock_vault):
    obj = AnsibleVaultEncryptedUnicode(ciphertext="dummy_ciphertext")
    obj.vault = mock_vault
    obj._ciphertext = "dummy_ciphertext"
    return obj

def test_ansible_vault_encrypted_unicode_eq_with_vault(ansible_vault_encrypted_unicode):
    other = "decrypted_data"
    assert ansible_vault_encrypted_unicode == other

def test_ansible_vault_encrypted_unicode_eq_without_vault():
    obj = AnsibleVaultEncryptedUnicode(ciphertext="dummy_ciphertext")
    obj.vault = None
    other = "decrypted_data"
    assert not (obj == other)
