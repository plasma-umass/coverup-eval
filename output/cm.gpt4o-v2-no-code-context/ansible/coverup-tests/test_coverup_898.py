# file: lib/ansible/parsing/yaml/objects.py:336-337
# asked: {"lines": [336, 337], "branches": []}
# gained: {"lines": [336, 337], "branches": []}

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
    return MockAnsibleVaultEncryptedUnicode("encrypted:data:with:colons")

def test_split_no_args(mock_ansible_vault_encrypted_unicode):
    result = mock_ansible_vault_encrypted_unicode.split()
    assert result == ["encrypted:data:with:colons"]

def test_split_with_sep(mock_ansible_vault_encrypted_unicode):
    result = mock_ansible_vault_encrypted_unicode.split(":")
    assert result == ["encrypted", "data", "with", "colons"]

def test_split_with_sep_and_maxsplit(mock_ansible_vault_encrypted_unicode):
    result = mock_ansible_vault_encrypted_unicode.split(":", 2)
    assert result == ["encrypted", "data", "with:colons"]
