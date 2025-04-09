# file: lib/ansible/parsing/yaml/objects.py:271-272
# asked: {"lines": [272], "branches": []}
# gained: {"lines": [272], "branches": []}

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
    return MockAnsibleVaultEncryptedUnicode("12345")

def test_isdigit_true(mock_ansible_vault_encrypted_unicode):
    assert mock_ansible_vault_encrypted_unicode.isdigit() is True

def test_isdigit_false():
    obj = MockAnsibleVaultEncryptedUnicode("abcde")
    assert obj.isdigit() is False
