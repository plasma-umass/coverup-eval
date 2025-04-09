# file lib/ansible/parsing/yaml/objects.py:345-346
# lines [345, 346]
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
    return MockAnsibleVaultEncryptedUnicode("vaulted_data")

def test_startswith(mock_ansible_vault_encrypted_unicode):
    obj = mock_ansible_vault_encrypted_unicode
    assert obj.startswith("vault") == True
    assert obj.startswith("data") == False
    assert obj.startswith("vault", 0, 5) == True
    assert obj.startswith("vault", 1) == False
    assert obj.startswith("vaulted_data", 0, 12) == True
    assert obj.startswith("vaulted_data", 0, 11) == False
