# file: lib/ansible/parsing/yaml/objects.py:245-248
# asked: {"lines": [245, 246, 247, 248], "branches": [[246, 247], [246, 248]]}
# gained: {"lines": [245, 246, 247, 248], "branches": [[246, 247], [246, 248]]}

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
def encrypted_unicode():
    return MockAnsibleVaultEncryptedUnicode("encrypted_data")

def test_find_with_string(encrypted_unicode):
    result = encrypted_unicode.find("data")
    assert result == 10

def test_find_with_ansible_vault_encrypted_unicode(encrypted_unicode):
    sub_encrypted_unicode = MockAnsibleVaultEncryptedUnicode("data")
    result = encrypted_unicode.find(sub_encrypted_unicode)
    assert result == 10

def test_find_with_start_and_end(encrypted_unicode):
    result = encrypted_unicode.find("data", 5, 15)
    assert result == 10
