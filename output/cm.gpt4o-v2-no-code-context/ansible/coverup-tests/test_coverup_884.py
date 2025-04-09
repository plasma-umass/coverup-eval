# file: lib/ansible/parsing/yaml/objects.py:231-232
# asked: {"lines": [231, 232], "branches": []}
# gained: {"lines": [231, 232], "branches": []}

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

def test_center_method(mock_ansible_vault_encrypted_unicode):
    centered_data = mock_ansible_vault_encrypted_unicode.center(20, '*')
    assert centered_data == "***encrypted_data***"
