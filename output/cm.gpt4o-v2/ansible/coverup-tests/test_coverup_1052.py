# file: lib/ansible/parsing/yaml/objects.py:259-260
# asked: {"lines": [259, 260], "branches": []}
# gained: {"lines": [259, 260], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def decrypt(self, ciphertext, obj=None):
        return "decryptedtext"

@pytest.fixture
def mock_vault():
    return MockVault()

@pytest.fixture
def encrypted_unicode(mock_vault, monkeypatch):
    obj = AnsibleVaultEncryptedUnicode("ciphertext")
    monkeypatch.setattr(obj, 'vault', mock_vault)
    monkeypatch.setattr(obj, '_ciphertext', b"ciphertext")
    return obj

def test_isalpha(encrypted_unicode):
    encrypted_unicode.data = "decryptedtext"
    assert encrypted_unicode.isalpha() == encrypted_unicode.data.isalpha()
