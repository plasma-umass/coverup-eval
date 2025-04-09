# file: lib/ansible/parsing/yaml/objects.py:277-278
# asked: {"lines": [277, 278], "branches": []}
# gained: {"lines": [277, 278], "branches": []}

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

def test_islower_true(mock_ansible_vault_encrypted_unicode):
    mock_ansible_vault_encrypted_unicode._data = "lowercase"
    assert mock_ansible_vault_encrypted_unicode.islower() is True

def test_islower_false(mock_ansible_vault_encrypted_unicode):
    mock_ansible_vault_encrypted_unicode._data = "NotLowerCase"
    assert mock_ansible_vault_encrypted_unicode.islower() is False
