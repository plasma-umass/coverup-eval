# file: lib/ansible/parsing/yaml/objects.py:175-178
# asked: {"lines": [175, 176, 177, 178], "branches": [[176, 177], [176, 178]]}
# gained: {"lines": [175, 176, 177, 178], "branches": [[176, 177], [176, 178]]}

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

def test_ansible_vault_encrypted_unicode_gt_same_type(mock_vault_unicode):
    other = MockAnsibleVaultEncryptedUnicode("other_encrypted_data")
    assert (mock_vault_unicode > other) == (mock_vault_unicode.data > other.data)

def test_ansible_vault_encrypted_unicode_gt_different_type(mock_vault_unicode):
    other = "other_encrypted_data"
    assert (mock_vault_unicode > other) == (mock_vault_unicode.data > other)
