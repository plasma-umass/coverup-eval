# file: lib/ansible/parsing/yaml/objects.py:301-302
# asked: {"lines": [301, 302], "branches": []}
# gained: {"lines": [301, 302], "branches": []}

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
    return MockAnsibleVaultEncryptedUnicode("ENCRYPTEDDATA")

def test_lower_method(mock_ansible_vault_encrypted_unicode):
    result = mock_ansible_vault_encrypted_unicode.lower()
    assert result == "encrypteddata"
