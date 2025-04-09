# file: lib/ansible/parsing/yaml/objects.py:208-211
# asked: {"lines": [208, 209, 210, 211], "branches": [[209, 210], [209, 211]]}
# gained: {"lines": [208, 209, 210, 211], "branches": [[209, 210], [209, 211]]}

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
def vault_unicode():
    return MockAnsibleVaultEncryptedUnicode("encrypted_data")

def test_radd_with_text_type(vault_unicode):
    result = "prefix_" + vault_unicode
    assert result == "prefix_encrypted_data"

def test_radd_with_non_text_type(vault_unicode):
    result = 123 + vault_unicode
    assert result == "123encrypted_data"
