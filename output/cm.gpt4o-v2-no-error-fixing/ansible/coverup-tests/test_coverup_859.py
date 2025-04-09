# file: lib/ansible/parsing/yaml/objects.py:152-153
# asked: {"lines": [153], "branches": []}
# gained: {"lines": [153], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def decrypt(self, ciphertext):
        return "123.45"

@pytest.fixture
def mock_vault(monkeypatch):
    def mock_decrypt(self, ciphertext):
        return "123.45"
    monkeypatch.setattr(MockVault, "decrypt", mock_decrypt)
    return MockVault()

def test_ansible_vault_encrypted_unicode_float(mock_vault):
    encrypted_unicode = AnsibleVaultEncryptedUnicode("encrypted_data")
    encrypted_unicode.vault = mock_vault
    encrypted_unicode._ciphertext = b"encrypted_data"
    
    # Mock the data property to return a decryptable string
    with pytest.MonkeyPatch.context() as m:
        m.setattr(AnsibleVaultEncryptedUnicode, "data", "123.45")
        result = float(encrypted_unicode)
        assert result == 123.45
