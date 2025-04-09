# file: lib/ansible/parsing/yaml/objects.py:250-251
# asked: {"lines": [250, 251], "branches": []}
# gained: {"lines": [250, 251], "branches": []}

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
    return MockAnsibleVaultEncryptedUnicode("Encrypted {0} data")

def test_format_method(mock_vault_unicode):
    formatted_data = mock_vault_unicode.format("test")
    assert formatted_data == "Encrypted test data"
