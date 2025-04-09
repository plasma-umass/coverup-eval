# file: lib/ansible/parsing/yaml/objects.py:262-263
# asked: {"lines": [263], "branches": []}
# gained: {"lines": [263], "branches": []}

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
    return MockAnsibleVaultEncryptedUnicode("encrypteddata123")

def test_isalnum(mock_ansible_vault_encrypted_unicode):
    assert mock_ansible_vault_encrypted_unicode.isalnum() == True

@pytest.fixture
def mock_ansible_vault_encrypted_unicode_non_alnum():
    return MockAnsibleVaultEncryptedUnicode("encrypted data!")

def test_isalnum_non_alnum(mock_ansible_vault_encrypted_unicode_non_alnum):
    assert mock_ansible_vault_encrypted_unicode_non_alnum.isalnum() == False
