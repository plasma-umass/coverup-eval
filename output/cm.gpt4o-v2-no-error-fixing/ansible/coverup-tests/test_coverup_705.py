# file: lib/ansible/parsing/yaml/objects.py:280-281
# asked: {"lines": [280, 281], "branches": []}
# gained: {"lines": [280, 281], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def decrypt(self, ciphertext):
        return "12345"

@pytest.fixture
def mock_vault(monkeypatch):
    def mock_data(self):
        return MockVault().decrypt(self._ciphertext)
    monkeypatch.setattr(AnsibleVaultEncryptedUnicode, 'data', property(mock_data))

def test_isnumeric(mock_vault):
    encrypted_unicode = AnsibleVaultEncryptedUnicode("dummy_ciphertext")
    assert encrypted_unicode.isnumeric() == True
