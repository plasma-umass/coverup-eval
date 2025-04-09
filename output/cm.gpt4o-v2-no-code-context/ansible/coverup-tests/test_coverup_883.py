# file: lib/ansible/parsing/yaml/objects.py:286-287
# asked: {"lines": [286, 287], "branches": []}
# gained: {"lines": [286, 287], "branches": []}

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
    return MockAnsibleVaultEncryptedUnicode("   ")

def test_isspace_true(mock_ansible_vault_encrypted_unicode):
    assert mock_ansible_vault_encrypted_unicode.isspace() == True

def test_isspace_false():
    obj = MockAnsibleVaultEncryptedUnicode("not only spaces")
    assert obj.isspace() == False
