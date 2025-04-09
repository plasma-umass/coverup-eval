# file: lib/ansible/parsing/yaml/objects.py:180-183
# asked: {"lines": [180, 181, 182, 183], "branches": [[181, 182], [181, 183]]}
# gained: {"lines": [180, 181, 182, 183], "branches": [[181, 182], [181, 183]]}

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
def mock_vault_unicode():
    return MockAnsibleVaultEncryptedUnicode("mock_data")

def test_ansible_vault_encrypted_unicode_ge_same_type(mock_vault_unicode):
    other = MockAnsibleVaultEncryptedUnicode("mock_data")
    assert mock_vault_unicode >= other

def test_ansible_vault_encrypted_unicode_ge_different_type(mock_vault_unicode):
    other = "mock_data"
    assert mock_vault_unicode >= other
