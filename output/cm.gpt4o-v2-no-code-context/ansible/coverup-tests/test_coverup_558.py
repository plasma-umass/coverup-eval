# file: lib/ansible/parsing/yaml/objects.py:319-322
# asked: {"lines": [319, 320, 321, 322], "branches": [[320, 321], [320, 322]]}
# gained: {"lines": [319, 320, 321, 322], "branches": [[320, 321], [320, 322]]}

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
    return MockAnsibleVaultEncryptedUnicode("This is a test string for AnsibleVaultEncryptedUnicode.")

def test_rfind_with_string(mock_vault_unicode):
    result = mock_vault_unicode.rfind("test")
    assert result == 10

def test_rfind_with_ansible_vault_encrypted_unicode(mock_vault_unicode):
    sub_vault_unicode = MockAnsibleVaultEncryptedUnicode("test")
    result = mock_vault_unicode.rfind(sub_vault_unicode)
    assert result == 10

def test_rfind_with_start_and_end(mock_vault_unicode):
    result = mock_vault_unicode.rfind("test", 0, 15)
    assert result == 10

def test_rfind_not_found(mock_vault_unicode):
    result = mock_vault_unicode.rfind("notfound")
    assert result == -1
