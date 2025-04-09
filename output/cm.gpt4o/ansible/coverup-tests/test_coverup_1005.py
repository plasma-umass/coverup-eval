# file lib/ansible/parsing/yaml/objects.py:336-337
# lines [336, 337]
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

@pytest.fixture
def mock_ansible_vault_encrypted_unicode():
    return MockAnsibleVaultEncryptedUnicode("encrypted_data_string")

def test_split(mock_ansible_vault_encrypted_unicode):
    result = mock_ansible_vault_encrypted_unicode.split('_')
    assert result == ["encrypted", "data", "string"]

    result = mock_ansible_vault_encrypted_unicode.split('_', 1)
    assert result == ["encrypted", "data_string"]

    result = mock_ansible_vault_encrypted_unicode.split()
    assert result == ["encrypted_data_string"]
