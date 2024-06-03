# file lib/ansible/parsing/yaml/objects.py:175-178
# lines [175, 176, 177, 178]
# branches ['176->177', '176->178']

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockAnsibleVaultEncryptedUnicode(AnsibleVaultEncryptedUnicode):
    def __init__(self, data):
        self._data = data
        self.vault = True  # Mock the vault attribute to avoid AttributeError

    @property
    def data(self):
        return self._data

@pytest.fixture
def mock_vault_unicode():
    return MockAnsibleVaultEncryptedUnicode("encrypted_data")

def test_ansible_vault_encrypted_unicode_gt(mock_vault_unicode):
    # Test comparison with another AnsibleVaultEncryptedUnicode instance
    other_vault_unicode = MockAnsibleVaultEncryptedUnicode("other_encrypted_data")
    assert (mock_vault_unicode > other_vault_unicode) == (mock_vault_unicode.data > other_vault_unicode.data)

    # Test comparison with a regular string
    assert (mock_vault_unicode > "some_string") == (mock_vault_unicode.data > "some_string")
