# file: lib/ansible/parsing/yaml/objects.py:348-349
# asked: {"lines": [348, 349], "branches": []}
# gained: {"lines": [348, 349], "branches": []}

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

def test_strip_no_chars(mock_ansible_vault_encrypted_unicode):
    result = mock_ansible_vault_encrypted_unicode.strip()
    assert result == "encrypted data"

def test_strip_with_chars(mock_ansible_vault_encrypted_unicode):
    result = mock_ansible_vault_encrypted_unicode.strip(" e")
    assert result == "ncrypted data"
