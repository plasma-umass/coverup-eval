# file lib/ansible/parsing/yaml/objects.py:286-287
# lines [286, 287]
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

def test_ansible_vault_encrypted_unicode_isspace():
    # Test case where data is all spaces
    obj = MockAnsibleVaultEncryptedUnicode("   ")
    assert obj.isspace() is True

    # Test case where data is not all spaces
    obj = MockAnsibleVaultEncryptedUnicode("abc")
    assert obj.isspace() is False

    # Test case where data is empty
    obj = MockAnsibleVaultEncryptedUnicode("")
    assert obj.isspace() is False
