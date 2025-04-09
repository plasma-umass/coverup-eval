# file lib/ansible/parsing/yaml/objects.py:333-334
# lines [333, 334]
# branches []

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
    return MockAnsibleVaultEncryptedUnicode("encrypted_data   ")

def test_ansible_vault_encrypted_unicode_rstrip(mock_ansible_vault_encrypted_unicode):
    # Test rstrip without chars argument
    result = mock_ansible_vault_encrypted_unicode.rstrip()
    assert result == "encrypted_data"

    # Test rstrip with chars argument
    result = mock_ansible_vault_encrypted_unicode.rstrip(" ")
    assert result == "encrypted_data"
