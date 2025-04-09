# file: lib/ansible/parsing/yaml/objects.py:218-219
# asked: {"lines": [218, 219], "branches": []}
# gained: {"lines": [218, 219], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockAnsibleVaultEncryptedUnicode(AnsibleVaultEncryptedUnicode):
    def __init__(self, data):
        self._data = data
        self.vault = True

    @property
    def data(self):
        return self._data

def test_ansible_vault_encrypted_unicode_mod():
    obj = MockAnsibleVaultEncryptedUnicode("Hello, %s!")
    result = obj % "World"
    assert result == "Hello, World!"
