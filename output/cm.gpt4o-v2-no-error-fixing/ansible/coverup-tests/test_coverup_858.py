# file: lib/ansible/parsing/yaml/objects.py:134-135
# asked: {"lines": [135], "branches": []}
# gained: {"lines": [135], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
from ansible.module_utils._text import to_native

class MockVault:
    def decrypt(self, ciphertext):
        return "decrypted_data"

@pytest.fixture
def mock_vault():
    return MockVault()

def test_ansible_vault_encrypted_unicode_str(mock_vault, monkeypatch):
    ciphertext = b"encrypted_data"
    obj = AnsibleVaultEncryptedUnicode(ciphertext)
    obj.vault = mock_vault

    # Mock the data property to return decrypted data
    monkeypatch.setattr(AnsibleVaultEncryptedUnicode, 'data', 'decrypted_data')

    result = str(obj)
    assert result == to_native('decrypted_data', errors='surrogate_or_strict')
