# file: lib/ansible/parsing/yaml/objects.py:304-305
# asked: {"lines": [304, 305], "branches": []}
# gained: {"lines": [304, 305], "branches": []}

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
    return MockAnsibleVaultEncryptedUnicode("  encrypted data  ")

def test_lstrip_no_chars(mock_ansible_vault_encrypted_unicode):
    result = mock_ansible_vault_encrypted_unicode.lstrip()
    assert result == "encrypted data  "

def test_lstrip_with_chars(mock_ansible_vault_encrypted_unicode):
    result = mock_ansible_vault_encrypted_unicode.lstrip(" e")
    assert result == "ncrypted data  "
