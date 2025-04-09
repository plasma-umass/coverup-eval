# file: lib/ansible/parsing/yaml/objects.py:333-334
# asked: {"lines": [333, 334], "branches": []}
# gained: {"lines": [333, 334], "branches": []}

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
    return MockAnsibleVaultEncryptedUnicode("  secret_data  ")

def test_ansible_vault_encrypted_unicode_rstrip(mock_ansible_vault_encrypted_unicode):
    result = mock_ansible_vault_encrypted_unicode.rstrip()
    assert result == "  secret_data"
    
    result_with_chars = mock_ansible_vault_encrypted_unicode.rstrip(" ")
    assert result_with_chars == "  secret_data"
    
    result_with_chars = mock_ansible_vault_encrypted_unicode.rstrip(" d")
    assert result_with_chars == "  secret_data"
