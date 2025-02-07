# file: lib/ansible/parsing/yaml/objects.py:363-364
# asked: {"lines": [363, 364], "branches": []}
# gained: {"lines": [363, 364], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def decrypt(self, ciphertext, obj=None):
        return "12345"

@pytest.fixture
def mock_vault():
    return MockVault()

@pytest.fixture
def encrypted_unicode(mock_vault, monkeypatch):
    obj = AnsibleVaultEncryptedUnicode("encrypted_data")
    monkeypatch.setattr(obj, 'vault', mock_vault)
    monkeypatch.setattr(obj, '_ciphertext', b"encrypted_data")
    return obj

def test_zfill(encrypted_unicode):
    result = encrypted_unicode.zfill(10)
    assert result == "0000012345"
