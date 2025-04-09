# file: lib/ansible/parsing/yaml/objects.py:354-355
# asked: {"lines": [354, 355], "branches": []}
# gained: {"lines": [354, 355], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def decrypt(self, ciphertext):
        return "decrypted text"

@pytest.fixture
def mock_vault(monkeypatch):
    def mock_data(self):
        return "mocked data"
    
    monkeypatch.setattr(AnsibleVaultEncryptedUnicode, 'data', property(mock_data))
    return AnsibleVaultEncryptedUnicode("ciphertext")

def test_title(mock_vault):
    assert mock_vault.title() == "mocked data".title()
