# file: lib/ansible/parsing/yaml/objects.py:309-310
# asked: {"lines": [309, 310], "branches": []}
# gained: {"lines": [309, 310], "branches": []}

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
    return MockAnsibleVaultEncryptedUnicode("encrypted:my_secret_data")

def test_partition(mock_ansible_vault_encrypted_unicode):
    result = mock_ansible_vault_encrypted_unicode.partition(":")
    assert result == ("encrypted", ":", "my_secret_data")
