# file: lib/ansible/parsing/yaml/objects.py:225-226
# asked: {"lines": [225, 226], "branches": []}
# gained: {"lines": [225, 226], "branches": []}

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
    return MockAnsibleVaultEncryptedUnicode("encrypted data")

def test_capitalize(mock_ansible_vault_encrypted_unicode):
    result = mock_ansible_vault_encrypted_unicode.capitalize()
    assert result == "Encrypted data"
