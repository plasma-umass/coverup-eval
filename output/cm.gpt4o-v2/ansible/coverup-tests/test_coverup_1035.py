# file: lib/ansible/parsing/yaml/objects.py:242-243
# asked: {"lines": [242, 243], "branches": []}
# gained: {"lines": [242, 243], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def decrypt(self, ciphertext):
        return "decrypted data"

@pytest.fixture
def mock_vault(monkeypatch):
    def mock_decrypt(self):
        return "decrypted data"
    monkeypatch.setattr(AnsibleVaultEncryptedUnicode, 'data', property(mock_decrypt))

def test_expandtabs(mock_vault):
    ciphertext = b"encrypted data"
    obj = AnsibleVaultEncryptedUnicode(ciphertext)
    result = obj.expandtabs(4)
    assert result == "decrypted data".expandtabs(4)
