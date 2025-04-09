# file lib/ansible/parsing/yaml/objects.py:312-317
# lines [312, 313, 314, 315, 316, 317]
# branches ['313->314', '313->315', '315->316', '315->317']

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockAnsibleVaultEncryptedUnicode(AnsibleVaultEncryptedUnicode):
    def __init__(self, data):
        self._data = data
        self.vault = True  # Mocking the vault attribute

    @property
    def data(self):
        return self._data

def test_replace_with_ansible_vault_encrypted_unicode():
    # Mocking the data attribute
    mock_old = MockAnsibleVaultEncryptedUnicode("old_value")
    mock_new = MockAnsibleVaultEncryptedUnicode("new_value")
    mock_self = MockAnsibleVaultEncryptedUnicode("this is an old_value string")

    # Perform the replace operation
    result = mock_self.replace(mock_old, mock_new)

    # Assert the result is as expected
    assert result == "this is an new_value string"

def test_replace_with_string():
    # Mocking the data attribute
    mock_self = MockAnsibleVaultEncryptedUnicode("this is an old_value string")

    # Perform the replace operation
    result = mock_self.replace("old_value", "new_value")

    # Assert the result is as expected
    assert result == "this is an new_value string"
