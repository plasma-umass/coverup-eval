# file lib/ansible/parsing/yaml/objects.py:213-214
# lines [214]
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

def test_ansible_vault_encrypted_unicode_mul():
    # Create an instance of the mock class with some data
    obj = MockAnsibleVaultEncryptedUnicode("secret")

    # Multiply the data
    result = obj.__mul__(3)

    # Assert the result is as expected
    assert result == "secretsecretsecret"

    # Clean up
    del obj
