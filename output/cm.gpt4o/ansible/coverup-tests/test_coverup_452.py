# file lib/ansible/parsing/yaml/objects.py:201-206
# lines [201, 202, 203, 204, 205, 206]
# branches ['202->203', '202->204', '204->205', '204->206']

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
from ansible.module_utils._text import to_text
from collections.abc import Sequence

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

def test_ansible_vault_encrypted_unicode_add_same_type(mock_ansible_vault_encrypted_unicode):
    other = MockAnsibleVaultEncryptedUnicode("other_encrypted_data")
    result = mock_ansible_vault_encrypted_unicode + other
    assert result == "encrypted_dataother_encrypted_data"

def test_ansible_vault_encrypted_unicode_add_text_type(mock_ansible_vault_encrypted_unicode):
    other = "plain_text_data"
    result = mock_ansible_vault_encrypted_unicode + other
    assert result == "encrypted_dataplain_text_data"

def test_ansible_vault_encrypted_unicode_add_other_type(mock_ansible_vault_encrypted_unicode):
    other = 12345
    result = mock_ansible_vault_encrypted_unicode + other
    assert result == "encrypted_data12345"
