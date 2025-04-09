# file: lib/ansible/parsing/yaml/objects.py:342-343
# asked: {"lines": [342, 343], "branches": []}
# gained: {"lines": [342, 343], "branches": []}

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
    return MockAnsibleVaultEncryptedUnicode("line1\nline2\nline3")

def test_splitlines_no_keepends(mock_vault_unicode):
    result = mock_vault_unicode.splitlines()
    assert result == ["line1", "line2", "line3"]

def test_splitlines_with_keepends(mock_vault_unicode):
    result = mock_vault_unicode.splitlines(keepends=True)
    assert result == ["line1\n", "line2\n", "line3"]
