# file: lib/ansible/parsing/yaml/objects.py:221-222
# asked: {"lines": [221, 222], "branches": []}
# gained: {"lines": [221], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
from ansible.module_utils._text import to_text

class MockVault:
    def decrypt(self, ciphertext, obj):
        return "decrypted_value"

class MockAnsibleVaultEncryptedUnicode(AnsibleVaultEncryptedUnicode):
    def __init__(self, value):
        super().__init__(value)
        self.vault = MockVault()  # Mocking the vault attribute with a MockVault instance

    def __getitem__(self, index):
        return self._ciphertext[index]

    def __len__(self):
        return len(self._ciphertext)

@pytest.fixture
def mock_vault_unicode():
    return MockAnsibleVaultEncryptedUnicode("encrypted_value")

def test_rmod(mock_vault_unicode):
    template = "The secret is: %s"
    result = template % mock_vault_unicode
    assert result == "The secret is: decrypted_value"
