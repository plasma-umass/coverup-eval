# file: lib/ansible/parsing/yaml/objects.py:298-299
# asked: {"lines": [298, 299], "branches": []}
# gained: {"lines": [298, 299], "branches": []}

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
    return MockAnsibleVaultEncryptedUnicode("test_data")

def test_ljust(mock_ansible_vault_encrypted_unicode):
    result = mock_ansible_vault_encrypted_unicode.ljust(20, '*')
    assert result == "test_data***********"
