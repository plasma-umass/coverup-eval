# file: lib/ansible/parsing/yaml/objects.py:256-257
# asked: {"lines": [257], "branches": []}
# gained: {"lines": [257], "branches": []}

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
    return MockAnsibleVaultEncryptedUnicode(data="encrypted_data")

def test_index_method(mock_ansible_vault_encrypted_unicode):
    # Test normal case
    assert mock_ansible_vault_encrypted_unicode.index("encrypted") == 0
    # Test with start and end
    assert mock_ansible_vault_encrypted_unicode.index("data", 0, 20) == 10
    # Test with start and end where substring is not found
    with pytest.raises(ValueError):
        mock_ansible_vault_encrypted_unicode.index("not_in_data", 0, 20)
