# file: lib/ansible/parsing/yaml/objects.py:213-214
# asked: {"lines": [213, 214], "branches": []}
# gained: {"lines": [213, 214], "branches": []}

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
    return MockAnsibleVaultEncryptedUnicode("test")

def test_ansible_vault_encrypted_unicode_mul(mock_ansible_vault_encrypted_unicode):
    result = mock_ansible_vault_encrypted_unicode * 3
    assert result == "testtesttest"
