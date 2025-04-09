# file: lib/ansible/parsing/yaml/objects.py:259-260
# asked: {"lines": [260], "branches": []}
# gained: {"lines": [260], "branches": []}

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
    return MockAnsibleVaultEncryptedUnicode("encrypteddata")

def test_isalpha_true(mock_ansible_vault_encrypted_unicode):
    mock_ansible_vault_encrypted_unicode._data = "encrypteddata"
    assert mock_ansible_vault_encrypted_unicode.isalpha() == True

def test_isalpha_false(mock_ansible_vault_encrypted_unicode):
    mock_ansible_vault_encrypted_unicode._data = "encrypted data 123"
    assert mock_ansible_vault_encrypted_unicode.isalpha() == False
