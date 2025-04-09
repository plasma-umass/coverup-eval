# file: lib/ansible/parsing/yaml/objects.py:295-296
# asked: {"lines": [295, 296], "branches": []}
# gained: {"lines": [295, 296], "branches": []}

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

def test_ansible_vault_encrypted_unicode_join(mock_ansible_vault_encrypted_unicode):
    seq = ["part1", "part2", "part3"]
    result = mock_ansible_vault_encrypted_unicode.join(seq)
    assert result == "part1encrypted_datapart2encrypted_datapart3"
