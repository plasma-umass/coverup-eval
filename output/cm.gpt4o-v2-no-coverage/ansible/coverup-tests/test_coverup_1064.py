# file: lib/ansible/parsing/yaml/objects.py:336-337
# asked: {"lines": [336, 337], "branches": []}
# gained: {"lines": [336, 337], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def decrypt(self, ciphertext, obj=None):
        return ciphertext.decode('utf-8')

@pytest.fixture
def mock_vault(monkeypatch):
    def mock_init(self, ciphertext):
        self.vault = MockVault()
        self._ciphertext = ciphertext

    monkeypatch.setattr(AnsibleVaultEncryptedUnicode, "__init__", mock_init)

def test_split(mock_vault):
    encrypted_unicode = AnsibleVaultEncryptedUnicode(b"hello world")
    result = encrypted_unicode.split()
    assert result == ["hello", "world"]

    result = encrypted_unicode.split(sep=" ")
    assert result == ["hello", "world"]

    result = encrypted_unicode.split(maxsplit=1)
    assert result == ["hello", "world"]

    result = encrypted_unicode.split(sep="o")
    assert result == ["hell", " w", "rld"]
