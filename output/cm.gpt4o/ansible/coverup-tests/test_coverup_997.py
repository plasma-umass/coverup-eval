# file lib/ansible/parsing/yaml/objects.py:277-278
# lines [277, 278]
# branches []

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockAnsibleVaultEncryptedUnicode(AnsibleVaultEncryptedUnicode):
    def __init__(self, data):
        self._data = data
        self.vault = True

    @property
    def data(self):
        return self._data

def test_ansible_vault_encrypted_unicode_islower():
    # Test case where data is all lowercase
    obj = MockAnsibleVaultEncryptedUnicode("lowercase")
    assert obj.islower() is True

    # Test case where data is not all lowercase
    obj = MockAnsibleVaultEncryptedUnicode("NotLowerCase")
    assert obj.islower() is False

    # Test case where data is empty
    obj = MockAnsibleVaultEncryptedUnicode("")
    assert obj.islower() is False
