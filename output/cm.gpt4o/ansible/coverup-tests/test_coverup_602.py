# file lib/ansible/parsing/yaml/objects.py:170-173
# lines [170, 171, 172, 173]
# branches ['171->172', '171->173']

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

def test_ansible_vault_encrypted_unicode_le_with_same_type(mock_vault_unicode):
    other = MockAnsibleVaultEncryptedUnicode("other_encrypted_data")
    assert (mock_vault_unicode <= other) == (mock_vault_unicode.data <= other.data)

def test_ansible_vault_encrypted_unicode_le_with_string(mock_vault_unicode):
    other = "other_encrypted_data"
    assert (mock_vault_unicode <= other) == (mock_vault_unicode.data <= other)
