# file: lib/ansible/parsing/yaml/objects.py:149-150
# asked: {"lines": [150], "branches": []}
# gained: {"lines": [150], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def decrypt(self, ciphertext, obj=None):
        return "12345"

@pytest.fixture
def encrypted_unicode():
    vault = MockVault()
    encrypted = AnsibleVaultEncryptedUnicode("encrypted_data")
    encrypted.vault = vault
    return encrypted

def test_ansible_vault_encrypted_unicode_int(encrypted_unicode):
    result = int(encrypted_unicode)
    assert result == 12345
