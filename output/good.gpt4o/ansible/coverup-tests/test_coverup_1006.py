# file lib/ansible/parsing/yaml/objects.py:239-240
# lines [239, 240]
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

def test_ansible_vault_encrypted_unicode_endswith(mock_ansible_vault_encrypted_unicode):
    assert mock_ansible_vault_encrypted_unicode.endswith("data")
    assert not mock_ansible_vault_encrypted_unicode.endswith("wrong")
    assert mock_ansible_vault_encrypted_unicode.endswith("crypted", 1, 9)
    assert not mock_ansible_vault_encrypted_unicode.endswith("crypt", 2, 8)
