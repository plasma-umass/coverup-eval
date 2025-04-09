# file: lib/ansible/parsing/yaml/objects.py:360-361
# asked: {"lines": [360, 361], "branches": []}
# gained: {"lines": [360, 361], "branches": []}

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

def test_upper_method(mock_ansible_vault_encrypted_unicode):
    result = mock_ansible_vault_encrypted_unicode.upper()
    assert result == "ENCRYPTED_DATA"
