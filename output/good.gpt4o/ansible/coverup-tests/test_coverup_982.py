# file lib/ansible/parsing/yaml/objects.py:193-194
# lines [193, 194]
# branches []

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockAnsibleVaultEncryptedUnicode(AnsibleVaultEncryptedUnicode):
    def __init__(self, data, vault=True):
        self._data = data
        self.vault = vault

    @property
    def data(self):
        if not self.vault:
            raise ValueError("Vault is not available")
        return self._data

@pytest.fixture
def mock_ansible_vault_encrypted_unicode():
    return MockAnsibleVaultEncryptedUnicode(data="encrypted_data")

def test_ansible_vault_encrypted_unicode_getitem(mock_ansible_vault_encrypted_unicode):
    assert mock_ansible_vault_encrypted_unicode[0] == "e"
    assert mock_ansible_vault_encrypted_unicode[1] == "n"
    assert mock_ansible_vault_encrypted_unicode[2] == "c"
    assert mock_ansible_vault_encrypted_unicode[3] == "r"
    assert mock_ansible_vault_encrypted_unicode[4] == "y"
    assert mock_ansible_vault_encrypted_unicode[5] == "p"
    assert mock_ansible_vault_encrypted_unicode[6] == "t"
    assert mock_ansible_vault_encrypted_unicode[7] == "e"
    assert mock_ansible_vault_encrypted_unicode[8] == "d"
    assert mock_ansible_vault_encrypted_unicode[9] == "_"
    assert mock_ansible_vault_encrypted_unicode[10] == "d"
    assert mock_ansible_vault_encrypted_unicode[11] == "a"
    assert mock_ansible_vault_encrypted_unicode[12] == "t"
    assert mock_ansible_vault_encrypted_unicode[13] == "a"

def test_ansible_vault_encrypted_unicode_no_vault():
    mock_obj = MockAnsibleVaultEncryptedUnicode(data="encrypted_data", vault=False)
    with pytest.raises(ValueError, match="Vault is not available"):
        _ = mock_obj.data
