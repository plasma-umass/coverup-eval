# file: lib/ansible/parsing/yaml/objects.py:363-364
# asked: {"lines": [363, 364], "branches": []}
# gained: {"lines": [363, 364], "branches": []}

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
    return MockAnsibleVaultEncryptedUnicode("12345")

def test_zfill(mock_ansible_vault_encrypted_unicode):
    result = mock_ansible_vault_encrypted_unicode.zfill(10)
    assert result == "0000012345"
