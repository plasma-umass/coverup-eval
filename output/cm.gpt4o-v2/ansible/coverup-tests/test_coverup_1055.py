# file: lib/ansible/parsing/yaml/objects.py:336-337
# asked: {"lines": [336, 337], "branches": []}
# gained: {"lines": [336, 337], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def decrypt(self, ciphertext, obj=None):
        return "decrypted data"

@pytest.fixture
def mock_vault():
    return MockVault()

@pytest.fixture
def encrypted_unicode(mock_vault, monkeypatch):
    obj = AnsibleVaultEncryptedUnicode("ciphertext")
    monkeypatch.setattr(obj, 'vault', mock_vault)
    return obj

def test_split(encrypted_unicode):
    result = encrypted_unicode.split()
    assert result == ["decrypted", "data"]

    result = encrypted_unicode.split(sep=" ")
    assert result == ["decrypted", "data"]

    result = encrypted_unicode.split(maxsplit=1)
    assert result == ["decrypted", "data"]

    result = encrypted_unicode.split(sep=" ", maxsplit=1)
    assert result == ["decrypted", "data"]
