# file: lib/ansible/parsing/yaml/objects.py:292-293
# asked: {"lines": [293], "branches": []}
# gained: {"lines": [293], "branches": []}

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

def test_isupper_true(mock_ansible_vault_encrypted_unicode):
    assert mock_ansible_vault_encrypted_unicode.isupper() == True

def test_isupper_false():
    mock_obj = MockAnsibleVaultEncryptedUnicode("encrypteddata")
    assert mock_obj.isupper() == False
