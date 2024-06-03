# file lib/ansible/parsing/yaml/objects.py:234-237
# lines [234, 235, 236, 237]
# branches ['235->236', '235->237']

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

def test_count_with_substring(mock_ansible_vault_encrypted_unicode):
    assert mock_ansible_vault_encrypted_unicode.count("data") == 1

def test_count_with_ansible_vault_encrypted_unicode(mock_ansible_vault_encrypted_unicode):
    sub = MockAnsibleVaultEncryptedUnicode("data")
    assert mock_ansible_vault_encrypted_unicode.count(sub) == 1

def test_count_with_start_and_end(mock_ansible_vault_encrypted_unicode):
    assert mock_ansible_vault_encrypted_unicode.count("data", 0, 15) == 1

def test_count_with_no_match(mock_ansible_vault_encrypted_unicode):
    assert mock_ansible_vault_encrypted_unicode.count("no_match") == 0
