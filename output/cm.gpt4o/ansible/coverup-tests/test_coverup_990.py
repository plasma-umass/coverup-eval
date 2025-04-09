# file lib/ansible/parsing/yaml/objects.py:271-272
# lines [271, 272]
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

def test_ansible_vault_encrypted_unicode_isdigit():
    # Test case where data is all digits
    encrypted_unicode = MockAnsibleVaultEncryptedUnicode("12345")
    assert encrypted_unicode.isdigit() is True

    # Test case where data is not all digits
    encrypted_unicode = MockAnsibleVaultEncryptedUnicode("123a45")
    assert encrypted_unicode.isdigit() is False

    # Test case where data is empty
    encrypted_unicode = MockAnsibleVaultEncryptedUnicode("")
    assert encrypted_unicode.isdigit() is False
