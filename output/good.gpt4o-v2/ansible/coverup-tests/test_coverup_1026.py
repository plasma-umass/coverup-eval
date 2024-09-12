# file: lib/ansible/parsing/yaml/objects.py:190-191
# asked: {"lines": [190, 191], "branches": []}
# gained: {"lines": [190, 191], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def decrypt(self, ciphertext):
        return "decrypted_data"

@pytest.fixture
def mock_vault():
    return MockVault()

def test_ansible_vault_encrypted_unicode_len(mock_vault, monkeypatch):
    ciphertext = b"encrypted_data"
    obj = AnsibleVaultEncryptedUnicode(ciphertext)
    obj.vault = mock_vault
    obj._ciphertext = ciphertext

    # Mock the data property to return a known value
    monkeypatch.setattr(obj.__class__, 'data', property(lambda self: "decrypted_data"))

    assert len(obj) == len("decrypted_data")
