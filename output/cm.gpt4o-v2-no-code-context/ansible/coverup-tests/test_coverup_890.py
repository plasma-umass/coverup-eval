# file: lib/ansible/parsing/yaml/objects.py:330-331
# asked: {"lines": [330, 331], "branches": []}
# gained: {"lines": [330, 331], "branches": []}

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
    return MockAnsibleVaultEncryptedUnicode("encrypted:data:example")

def test_rpartition(mock_ansible_vault_encrypted_unicode):
    result = mock_ansible_vault_encrypted_unicode.rpartition(':')
    assert result == ('encrypted:data', ':', 'example')
