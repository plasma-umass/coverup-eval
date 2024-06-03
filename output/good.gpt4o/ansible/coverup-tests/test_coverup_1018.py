# file lib/ansible/parsing/yaml/objects.py:327-328
# lines [327, 328]
# branches []

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

def test_ansible_vault_encrypted_unicode_rjust(mock_ansible_vault_encrypted_unicode):
    result = mock_ansible_vault_encrypted_unicode.rjust(20, '*')
    assert result == "******encrypted_data"
