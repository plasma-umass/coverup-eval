# file: lib/ansible/parsing/yaml/objects.py:152-153
# asked: {"lines": [152, 153], "branches": []}
# gained: {"lines": [152, 153], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def decrypt(self, ciphertext, obj=None):
        return "123.45"

@pytest.fixture
def mock_vault(monkeypatch):
    def mock_decrypt(self, ciphertext, obj=None):
        return "123.45"
    monkeypatch.setattr(MockVault, "decrypt", mock_decrypt)
    return MockVault()

def test_ansible_vault_encrypted_unicode_float(mock_vault):
    ciphertext = b"dummy_ciphertext"
    obj = AnsibleVaultEncryptedUnicode(ciphertext)
    obj.vault = mock_vault
    obj._ciphertext = ciphertext

    # Mock the data property to return a decryptable string
    with pytest.MonkeyPatch.context() as m:
        m.setattr(obj, 'data', "123.45")
        result = float(obj)
        assert result == 123.45
