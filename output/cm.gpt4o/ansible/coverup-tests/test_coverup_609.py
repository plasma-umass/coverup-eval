# file lib/ansible/parsing/yaml/objects.py:319-322
# lines [319, 320, 321, 322]
# branches ['320->321', '320->322']

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
    return MockAnsibleVaultEncryptedUnicode("This is a test string for AnsibleVaultEncryptedUnicode.")

def test_rfind_with_string(mock_ansible_vault_encrypted_unicode):
    result = mock_ansible_vault_encrypted_unicode.rfind("test")
    assert result == 10

def test_rfind_with_ansible_vault_encrypted_unicode(mock_ansible_vault_encrypted_unicode):
    sub = MockAnsibleVaultEncryptedUnicode("test")
    result = mock_ansible_vault_encrypted_unicode.rfind(sub)
    assert result == 10

def test_rfind_with_start_and_end(mock_ansible_vault_encrypted_unicode):
    result = mock_ansible_vault_encrypted_unicode.rfind("test", 0, 15)
    assert result == 10

def test_rfind_not_found(mock_ansible_vault_encrypted_unicode):
    result = mock_ansible_vault_encrypted_unicode.rfind("notfound")
    assert result == -1
