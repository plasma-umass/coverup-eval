# file: lib/ansible/parsing/yaml/objects.py:201-206
# asked: {"lines": [201, 202, 203, 204, 205, 206], "branches": [[202, 203], [202, 204], [204, 205], [204, 206]]}
# gained: {"lines": [201, 202, 203, 204, 205, 206], "branches": [[202, 203], [202, 204], [204, 205], [204, 206]]}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
from ansible.module_utils._text import to_text

class MockAnsibleVaultEncryptedUnicode(AnsibleVaultEncryptedUnicode):
    def __init__(self, data):
        self._data = data
        self.vault = True

    @property
    def data(self):
        return self._data

@pytest.fixture
def mock_vault_unicode():
    return MockAnsibleVaultEncryptedUnicode("encrypted_data")

def test_add_with_same_type(mock_vault_unicode):
    other = MockAnsibleVaultEncryptedUnicode("more_data")
    result = mock_vault_unicode + other
    assert result == "encrypted_data" + "more_data"

def test_add_with_text_type(mock_vault_unicode):
    other = "plain_text"
    result = mock_vault_unicode + other
    assert result == "encrypted_data" + "plain_text"

def test_add_with_other_type(mock_vault_unicode):
    other = 12345
    result = mock_vault_unicode + other
    assert result == "encrypted_data" + to_text(12345)
