# file: lib/ansible/parsing/yaml/objects.py:140-141
# asked: {"lines": [141], "branches": []}
# gained: {"lines": [141], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
from ansible.module_utils._text import to_bytes

class MockAnsibleVaultEncryptedUnicode(AnsibleVaultEncryptedUnicode):
    def __init__(self, data, vault=True):
        self._data = data
        self.vault = vault

    @property
    def data(self):
        if not self.vault:
            raise ValueError("Vault is not set")
        return self._data

@pytest.fixture
def mock_ansible_vault_encrypted_unicode():
    return MockAnsibleVaultEncryptedUnicode("test_data")

def test_encode(mock_ansible_vault_encrypted_unicode, mocker):
    mock_to_bytes = mocker.patch('ansible.parsing.yaml.objects.to_bytes', return_value=b'test_data')
    result = mock_ansible_vault_encrypted_unicode.encode(encoding='utf-8', errors='strict')
    mock_to_bytes.assert_called_once_with("test_data", encoding='utf-8', errors='strict')
    assert result == b'test_data'
