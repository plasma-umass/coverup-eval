# file lib/ansible/parsing/yaml/objects.py:180-183
# lines [180, 181, 182, 183]
# branches ['181->182', '181->183']

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockAnsibleVaultEncryptedUnicode(AnsibleVaultEncryptedUnicode):
    def __init__(self, data):
        self._data = data
        self.vault = True

    @property
    def data(self):
        return self._data

@pytest.fixture
def mock_vault_unicode():
    return MockAnsibleVaultEncryptedUnicode("encrypted_data")

def test_ansible_vault_encrypted_unicode_ge_with_same_type(mock_vault_unicode):
    other = MockAnsibleVaultEncryptedUnicode("another_encrypted_data")
    assert (mock_vault_unicode >= other) == (mock_vault_unicode.data >= other.data)

def test_ansible_vault_encrypted_unicode_ge_with_string(mock_vault_unicode):
    other = "another_encrypted_data"
    assert (mock_vault_unicode >= other) == (mock_vault_unicode.data >= other)
