# file: lib/ansible/parsing/yaml/objects.py:339-340
# asked: {"lines": [339, 340], "branches": []}
# gained: {"lines": [339, 340], "branches": []}

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

def test_rsplit_no_sep(mock_ansible_vault_encrypted_unicode):
    result = mock_ansible_vault_encrypted_unicode.rsplit()
    assert result == ["encrypted:data:with:colons"]

def test_rsplit_with_sep(mock_ansible_vault_encrypted_unicode):
    result = mock_ansible_vault_encrypted_unicode.rsplit(":")
    assert result == ["encrypted", "data", "with", "colons"]

def test_rsplit_with_sep_and_maxsplit(mock_ansible_vault_encrypted_unicode):
    result = mock_ansible_vault_encrypted_unicode.rsplit(":", 1)
    assert result == ["encrypted:data:with", "colons"]
