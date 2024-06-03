# file lib/ansible/parsing/yaml/objects.py:165-168
# lines [165, 166, 167, 168]
# branches ['166->167', '166->168']

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockAnsibleVaultEncryptedUnicode(AnsibleVaultEncryptedUnicode):
    def __init__(self, data):
        self._data = data
        self.vault = True

    @property
    def data(self):
        return self._data

def test_ansible_vault_encrypted_unicode_lt():
    obj1 = MockAnsibleVaultEncryptedUnicode("abc")
    obj2 = MockAnsibleVaultEncryptedUnicode("def")
    obj3 = MockAnsibleVaultEncryptedUnicode("abc")

    # Test comparison with another AnsibleVaultEncryptedUnicode object
    assert obj1 < obj2
    assert not obj2 < obj1
    assert not obj1 < obj3

    # Test comparison with a regular string
    assert obj1 < "def"
    assert not obj2 < "abc"
    assert not obj1 < "abc"
