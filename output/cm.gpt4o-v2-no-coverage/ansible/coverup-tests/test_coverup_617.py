# file: lib/ansible/parsing/yaml/objects.py:106-110
# asked: {"lines": [106, 107, 108, 109, 110], "branches": [[108, 109], [108, 110]]}
# gained: {"lines": [106, 107, 108, 109, 110], "branches": [[108, 109], [108, 110]]}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
from ansible.module_utils._text import to_text

class MockVault:
    def decrypt(self, ciphertext, obj=None):
        return b"decrypted_" + ciphertext

@pytest.fixture
def mock_vault():
    return MockVault()

def test_ansible_vault_encrypted_unicode_data_with_vault(mock_vault):
    ciphertext = b"encrypted_data"
    obj = AnsibleVaultEncryptedUnicode(ciphertext)
    obj.vault = mock_vault

    assert obj.data == "decrypted_encrypted_data"

def test_ansible_vault_encrypted_unicode_data_without_vault():
    ciphertext = b"encrypted_data"
    obj = AnsibleVaultEncryptedUnicode(ciphertext)

    assert obj.data == "encrypted_data"
