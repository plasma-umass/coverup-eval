# file lib/ansible/parsing/yaml/objects.py:280-281
# lines [280, 281]
# branches []

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockAnsibleVaultEncryptedUnicode(AnsibleVaultEncryptedUnicode):
    def __init__(self, data):
        self._data = data
        self.vault = True  # Mocking the vault attribute

    @property
    def data(self):
        return self._data

def test_ansible_vault_encrypted_unicode_isnumeric():
    # Test with numeric data
    numeric_data = MockAnsibleVaultEncryptedUnicode("12345")
    assert numeric_data.isnumeric() is True

    # Test with non-numeric data
    non_numeric_data = MockAnsibleVaultEncryptedUnicode("abc123")
    assert non_numeric_data.isnumeric() is False

    # Test with empty data
    empty_data = MockAnsibleVaultEncryptedUnicode("")
    assert empty_data.isnumeric() is False
