# file lib/ansible/parsing/yaml/objects.py:185-188
# lines [185, 186, 187, 188]
# branches ['186->187', '186->188']

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

def test_ansible_vault_encrypted_unicode_contains(mock_ansible_vault_encrypted_unicode):
    # Test with a string that is in the data
    assert 'encrypted' in mock_ansible_vault_encrypted_unicode

    # Test with a string that is not in the data
    assert 'not_in_data' not in mock_ansible_vault_encrypted_unicode

    # Test with an instance of AnsibleVaultEncryptedUnicode containing data that is in the data
    another_instance = MockAnsibleVaultEncryptedUnicode("encrypted")
    assert another_instance in mock_ansible_vault_encrypted_unicode

    # Test with an instance of AnsibleVaultEncryptedUnicode containing data that is not in the data
    another_instance = MockAnsibleVaultEncryptedUnicode("not_in_data")
    assert another_instance not in mock_ansible_vault_encrypted_unicode
