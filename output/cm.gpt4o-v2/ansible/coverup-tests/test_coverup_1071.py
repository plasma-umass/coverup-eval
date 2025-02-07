# file: lib/ansible/parsing/yaml/objects.py:342-343
# asked: {"lines": [342, 343], "branches": []}
# gained: {"lines": [342, 343], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def decrypt(self, ciphertext, obj=None):
        return "line1\nline2\nline3"

@pytest.fixture
def mock_vault():
    return MockVault()

@pytest.fixture
def encrypted_unicode(mock_vault, monkeypatch):
    obj = AnsibleVaultEncryptedUnicode("ciphertext")
    monkeypatch.setattr(obj, 'vault', mock_vault)
    monkeypatch.setattr(obj, '_ciphertext', b"ciphertext")
    return obj

def test_splitlines_no_keepends(encrypted_unicode):
    result = encrypted_unicode.splitlines()
    assert result == ["line1", "line2", "line3"]

def test_splitlines_with_keepends(encrypted_unicode):
    result = encrypted_unicode.splitlines(keepends=True)
    assert result == ["line1\n", "line2\n", "line3"]
