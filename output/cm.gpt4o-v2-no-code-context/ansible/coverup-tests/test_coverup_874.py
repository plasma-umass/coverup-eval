# file: lib/ansible/parsing/yaml/objects.py:242-243
# asked: {"lines": [242, 243], "branches": []}
# gained: {"lines": [242, 243], "branches": []}

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
    return MockAnsibleVaultEncryptedUnicode("some\ttext")

def test_expandtabs(mock_ansible_vault_encrypted_unicode):
    result = mock_ansible_vault_encrypted_unicode.expandtabs(4)
    assert result == "some    text"
