# file: lib/ansible/parsing/yaml/objects.py:134-135
# asked: {"lines": [134, 135], "branches": []}
# gained: {"lines": [134, 135], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
from ansible.module_utils._text import to_native

class MockVault:
    def decrypt(self, ciphertext, obj=None):
        return "decrypted_data"

@pytest.fixture
def mock_vault(monkeypatch):
    def mock_decrypt(self, ciphertext, obj=None):
        return "decrypted_data"
    monkeypatch.setattr(MockVault, 'decrypt', mock_decrypt)

def test_ansible_vault_encrypted_unicode_str(mock_vault):
    ciphertext = b"encrypted_data"
    obj = AnsibleVaultEncryptedUnicode(ciphertext)
    obj.vault = MockVault()
    
    result = str(obj)
    
    assert result == "decrypted_data"
