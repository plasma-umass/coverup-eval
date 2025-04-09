# file: lib/ansible/parsing/yaml/objects.py:345-346
# asked: {"lines": [345, 346], "branches": []}
# gained: {"lines": [345, 346], "branches": []}

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
    return MockAnsibleVaultEncryptedUnicode("encrypted_data")

def test_startswith_full(mock_ansible_vault_encrypted_unicode):
    assert mock_ansible_vault_encrypted_unicode.startswith("encrypted") == True

def test_startswith_partial(mock_ansible_vault_encrypted_unicode):
    assert mock_ansible_vault_encrypted_unicode.startswith("data", start=10) == True

def test_startswith_false(mock_ansible_vault_encrypted_unicode):
    assert mock_ansible_vault_encrypted_unicode.startswith("wrong") == False
