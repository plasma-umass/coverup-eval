# file: lib/ansible/parsing/yaml/objects.py:185-188
# asked: {"lines": [185, 186, 187, 188], "branches": [[186, 187], [186, 188]]}
# gained: {"lines": [185, 186, 187, 188], "branches": [[186, 187], [186, 188]]}

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
def mock_vault_unicode():
    return MockAnsibleVaultEncryptedUnicode("encrypted_data")

def test_contains_with_string(mock_vault_unicode):
    assert 'e' in mock_vault_unicode
    assert 'z' not in mock_vault_unicode

def test_contains_with_vault_unicode(mock_vault_unicode):
    another_vault_unicode = MockAnsibleVaultEncryptedUnicode("encrypted")
    assert another_vault_unicode in mock_vault_unicode

def test_contains_with_non_vault_unicode(mock_vault_unicode):
    non_vault_unicode = "data"
    assert non_vault_unicode in mock_vault_unicode
