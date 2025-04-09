# file: lib/ansible/parsing/yaml/objects.py:295-296
# asked: {"lines": [295, 296], "branches": []}
# gained: {"lines": [295, 296], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def decrypt(self, ciphertext, obj=None):
        return "decrypted_text"

@pytest.fixture
def mock_vault():
    return MockVault()

def test_join(mock_vault):
    encrypted_text = AnsibleVaultEncryptedUnicode("ciphertext")
    encrypted_text.vault = mock_vault
    result = encrypted_text.join(["a", "b", "c"])
    assert result == "decrypted_text".join(["a", "b", "c"])

