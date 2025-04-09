# file: lib/ansible/parsing/yaml/objects.py:228-229
# asked: {"lines": [228, 229], "branches": []}
# gained: {"lines": [228, 229], "branches": []}

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
    return MockAnsibleVaultEncryptedUnicode("TestString")

def test_casefold(mock_ansible_vault_encrypted_unicode):
    result = mock_ansible_vault_encrypted_unicode.casefold()
    assert result == "teststring"
