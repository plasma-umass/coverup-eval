# file: lib/ansible/parsing/yaml/objects.py:234-237
# asked: {"lines": [234, 235, 236, 237], "branches": [[235, 236], [235, 237]]}
# gained: {"lines": [234, 235, 236, 237], "branches": [[235, 236], [235, 237]]}

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

def test_count_with_sub_as_string(mock_ansible_vault_encrypted_unicode):
    result = mock_ansible_vault_encrypted_unicode.count("encrypted")
    assert result == 1

def test_count_with_sub_as_ansible_vault_encrypted_unicode(mock_ansible_vault_encrypted_unicode):
    sub = MockAnsibleVaultEncryptedUnicode("encrypted")
    result = mock_ansible_vault_encrypted_unicode.count(sub)
    assert result == 1

def test_count_with_start_and_end(mock_ansible_vault_encrypted_unicode):
    result = mock_ansible_vault_encrypted_unicode.count("encrypted", 0, 10)
    assert result == 1
